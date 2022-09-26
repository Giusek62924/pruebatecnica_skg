import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { BrowserModule } from "@angular/platform-browser";
import { Routes, RouterModule } from "@angular/router";
const routes: Routes = [
  {
    path: "",
    redirectTo: "pages/login",
    pathMatch: "full",
  },
  {
    path: "",
    children: [
      {
        path: "tables",
        loadChildren: () =>
          import("./tables/tables.module").then(
            (m) => m.TablesModule
          ),
      },
    ],
  },
  {
    path: "",
    children: [
      {
        path: "pages",
        loadChildren: () =>
          import("./pages/pages.module").then(
            (m) => m.PagesModule
          ),
      },
    ],
  },
  {
    path: "**",
    redirectTo: "pages/login",
  },
];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes, {
      useHash: true,
      anchorScrolling: "enabled",
      relativeLinkResolution: "corrected",
      scrollPositionRestoration: "enabled",
      scrollOffset: [0, 0],
    }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
