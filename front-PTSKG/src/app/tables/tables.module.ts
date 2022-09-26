import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CommonModule } from "@angular/common";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { MasterComponent } from "./master/master.component"
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { ModalModule } from "ngx-bootstrap/modal";
import { TabsModule } from "ngx-bootstrap/tabs";

import { TablesRoutes } from "./tables.routing";

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule.withConfig({ warnOnNgModelWithFormControl: "never" }),
    RouterModule.forChild(TablesRoutes),
    TabsModule.forRoot(),
    ModalModule.forRoot()
  ],
  declarations: [MasterComponent]
})
export class TablesModule {}