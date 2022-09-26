import { Component, OnInit, OnDestroy } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { ToastrService } from "ngx-toastr";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Router } from "@angular/router"
//import { NotificationsComponent } from "../../components/notifications/notifications.component";
import { Servers } from "../../servers.component";
import { NotificationsComponent } from "../../component/notifications/notifications.component";

@Component({
  providers: [NotificationsComponent],
  selector: "app-login",
  templateUrl: "login.component.html",
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit, OnDestroy {
  focus : any;
  focus1 : any;

  focusTouched : any;
  focus1Touched : any;

  public PreloadInfo = false;
  public FlagPassword = null;
  public Encrypt = null;

  public formLogIn: any = FormGroup;
  constructor(public formBuilder: FormBuilder, public toastr: ToastrService, private http: HttpClient, private router: Router, private notification: NotificationsComponent) { }

  ngOnInit() {
    localStorage.clear();

    this.formLogIn = this.formBuilder.group({
      username: ["", [Validators.required, Validators.minLength(1)]],
      password: ["", [Validators.required, Validators.minLength(1)]],
    });
  }
  get loginF() {
    return this.formLogIn.controls;
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("login-page");
  }
  onLogin() {
    this.PreloadInfo = true;
    if (this.formLogIn.invalid) {
      this.notification.showNotification(
        "top",
        "right",
        1,
        "tim-icons icon-check-2",
        "Faltan datos por completar"
      );
      this.PreloadInfo = false;
      return;
    }
    this.FlagPassword = this.formLogIn.value.password;
    this.Encrypt = this.formLogIn.value.password;
    this.formLogIn.value.username = this.formLogIn.value.username.trim();
    // console.log(this.formLogIn.value)
    this.http
      .post(Servers.Deploy + "/login/", this.formLogIn.value, {
        headers: new HttpHeaders({
          "Content-Type": "application/json"
        }),
      })
      .subscribe(
        (response) => {
          var usuario = (response as any);
          this.notification.showNotification(
            "top",
            "right",
            2,
            "tim-icons icon-check-2",
            "Bienvenido " + usuario.user + "!."
          );
          let token = 'Bearer ' + (response as any).token;

          localStorage.clear();
          localStorage.setItem('token', usuario.token);
          localStorage.setItem('nombre', usuario.user);
          window.location.replace("/#/tables/TableM");
        },
        (e) => {
          var msg = (e.statusText == 'Not Found') ? 'Contraseña no valida/ Usuario no existe' : 'Se ha presentado un error, intentalo nuevamente';
          this.notification.showNotification(
            "top",
            "right",
            4,
            "tim-icons icon-simple-remove",
            msg
          );
          this.PreloadInfo = false;
        }
      );
  }
}
