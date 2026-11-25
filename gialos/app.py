"""App controller: owns the state and re-renders the current screen."""

import asyncio
from typing import Optional

import flet as ft

from gialos import i18n, state as st, theme
from gialos.components.top_bar import build_top_bar
from gialos.data.ranking import Recommendation, recommend
from gialos.images import WINDOW_ICON
from gialos.views import beach_detail, map_view, onboarding, recommended

# Screen -> view builder
VIEWS = {
    st.ONBOARDING: onboarding.build,
    st.RECOMMENDED: recommended.build,
    st.MAP: map_view.build,
    st.DETAIL: beach_detail.build,
}

MATCHING_SECONDS = 1.6   # how long "finding your beach" is shown


class GialosApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.state = st.AppState()
        self._reveal_target: Optional[ft.Control] = None
        self._setup_page()
        self.render()

    def _setup_page(self) -> None:
        page = self.page
        page.title = "gialos"
        page.theme = theme.app_theme()
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = theme.BACKGROUND
        page.padding = 0
        page.on_resize = lambda _: self._on_resize()
        self._framed = self._wants_frame()
        if not page.web:
            page.window.width = theme.PHONE_WIDTH
            page.window.height = theme.PHONE_HEIGHT
            page.window.icon = str(WINDOW_ICON)   # Windows only; ignored elsewhere

    # --- Rendering ---------------------------------------------------------
    def _wants_frame(self) -> bool:
        """Draw a phone frame only in a wide browser window; on a phone or in the
        phone-sized desktop window the app fills the screen."""
        return bool(self.page.web) and (self.page.width or 0) > theme.FRAME_BREAKPOINT

    def _on_resize(self) -> None:
        self._framed = self._wants_frame()
        self.render()

    def render(self) -> None:
        """Rebuild the whole current screen (cheap for a mockup, keeps code simple)."""
        screen = self.state.screen
        parts: list[ft.Control] = [
            build_top_bar(
                self.state,
                self.toggle_language,
                on_back=self.go_back if screen == st.DETAIL else None,
            ),
            ft.Container(content=VIEWS[screen](self), expand=True),
        ]
        if screen in st.TABS:
            parts.append(self._navigation_bar())
        app_screen = ft.Column(parts, spacing=0, expand=True)
        self.page.controls = [self._phone_frame(app_screen) if self._framed else ft.SafeArea(app_screen, expand=True)]
        self.page.update()
        if self._reveal_target is not None:
            self.page.run_task(self._play_reveal, self._reveal_target)
            self._reveal_target = None

    def _phone_frame(self, app_screen: ft.Control) -> ft.Control:
        """Centre the app in a phone-shaped frame on a soft backdrop."""
        height = min(theme.PHONE_HEIGHT, (self.page.height or theme.PHONE_HEIGHT) - 2 * theme.FRAME_MARGIN)
        phone = ft.Container(
            content=ft.Container(
                content=app_screen,
                bgcolor=theme.BACKGROUND,
                border_radius=theme.FRAME_RADIUS - theme.FRAME_BEZEL,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            ),
            width=theme.PHONE_WIDTH + 2 * theme.FRAME_BEZEL,
            height=height,
            padding=theme.FRAME_BEZEL,
            bgcolor=theme.FRAME_BEZEL_COLOR,
            border_radius=theme.FRAME_RADIUS,
            shadow=ft.BoxShadow(blur_radius=48, spread_radius=2, color=theme.SHADOW, offset=ft.Offset(0, 20)),
        )
        return ft.Container(
            content=phone,
            alignment=ft.Alignment.CENTER,
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=list(theme.FRAME_BACKDROP),
            ),
        )

    def _navigation_bar(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.AUTO_AWESOME_OUTLINED,
                    selected_icon=ft.Icons.AUTO_AWESOME,
                    label=self.state.t("nav_recommended"),
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.MAP_OUTLINED,
                    selected_icon=ft.Icons.MAP,
                    label=self.state.t("nav_map"),
                ),
            ],
            selected_index=st.TABS.index(self.state.current_tab),
            bgcolor=theme.SURFACE,
            indicator_color=theme.ACCENT_12,
            elevation=0,
            border=ft.Border.only(top=ft.BorderSide(1, theme.LINE)),
            on_change=lambda e: self.select_tab(st.TABS[e.control.selected_index]),
        )

    # --- Result animation (the "peak" moment) -------------------------------
    def queue_reveal(self, control: ft.Control) -> None:
        """Called by a view: animate `control` in right after it is shown."""
        self._reveal_target = control

    async def _play_reveal(self, control: ft.Control) -> None:
        await asyncio.sleep(0.05)
        control.scale = 1
        control.update()
        self.state.reveal_pending = False

    # --- Queries -----------------------------------------------------------
    def recommendation(self) -> Recommendation:
        p = self.state.preferences
        return recommend(p.surface, p.vibe, p.wind_tolerance, p.day_index)

    # --- Actions -----------------------------------------------------------
    def toggle_language(self) -> None:
        self.state.language = i18n.other_language(self.state.language)
        self.render()

    def onboarding_next(self) -> None:
        if self.state.onboarding_step < len(onboarding.QUESTIONS):
            self.state.onboarding_step += 1
            self.render()
        else:
            self.page.run_task(self._match)

    def onboarding_back(self) -> None:
        self.state.onboarding_step = max(0, self.state.onboarding_step - 1)
        self.render()

    async def _match(self) -> None:
        """Show "finding your beach", then reveal the result."""
        self.state.matching = True
        self.render()
        await asyncio.sleep(MATCHING_SECONDS)
        self.state.matching = False
        self.state.reveal_pending = True
        self.select_tab(st.RECOMMENDED)

    def change_answers(self) -> None:
        self.state.screen = st.ONBOARDING
        self.state.onboarding_step = 1
        self.render()

    def select_tab(self, tab: str) -> None:
        self.state.current_tab = tab
        self.state.screen = tab
        self.render()

    def open_beach(self, beach_id: str) -> None:
        self.state.selected_beach_id = beach_id
        self.state.screen = st.DETAIL
        self.render()

    def go_back(self) -> None:
        self.state.screen = self.state.current_tab
        self.render()
