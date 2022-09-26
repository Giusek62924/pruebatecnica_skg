import { Routes } from "@angular/router";

import { MasterComponent } from './master/master.component';

export const TablesRoutes: Routes = [
  {
    path: "",
    children: [
      {
        path: "TableM",
        component: MasterComponent  
      }
    ]
  }
];
