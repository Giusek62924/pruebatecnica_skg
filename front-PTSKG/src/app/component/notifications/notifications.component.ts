import { Component } from "@angular/core";
import { ToastrService } from "ngx-toastr";
import { Router } from "@angular/router";
import swal from "sweetalert2";

@Component({
  selector: "app-notifications",
  templateUrl: "notifications.component.html",
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent {
  constructor(public toastr: ToastrService, private router: Router) {}
  ngOnInit() {
  }

  public showNotification(from : any, align : any, color : any, icon : any, message : any) {
    switch (color) {
      case 1:
        this.toastr.info(message);
        break;
      case 2:
        this.toastr.success(message);
        break;
      case 3:
        this.toastr.warning(
          '<span class="' + icon + '"></span>' + message + "</b>",
          "",
          {
            timeOut: 8000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-warning alert-with-icon",
            positionClass: "toast-" + from + "-" + align,
          }
        );
        break;
      case 4:
        this.toastr.error(message);
        break;
      case 5:
        this.toastr.show(
          '<span class="' + icon + '"></span>' + message + "</b>",
          "",
          {
            timeOut: 8000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-primary alert-with-icon",
            positionClass: "toast-" + from + "-" + align,
          }
        );
        break;
      default:
        break;
    }
  }
}

