import {
  BsModalRef,
  ModalOptions,
  BsModalService,
  ModalDirective,
} from "ngx-bootstrap/modal";
import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
//import { NotificationsComponent } from "../../components/notifications/notifications.component";
import { Servers } from '../../servers.component';
import { NotificationsComponent } from '../../component/notifications/notifications.component';

@Component({
  providers: [NotificationsComponent],
  selector: 'app-master',
  templateUrl: './master.component.html',
  styleUrls: ['./master.component.css'],
})
export class MasterComponent implements OnInit {
  public List: any;

  public entity = ['BANCOLOMBIA', 'COLPATRIA', 'DAVIVIENDA'];

  public role = ['CLIENTE', 'USUARIO', 'ADMINISTRADOR'];

  public city = ['BOGOTÂ', 'BARRANQUILLA', 'SANTA MARTA'];

  focusTouched1 : any;
  focus1 : any;
  focusTouched2 : any;
  focus2 : any;
  focusTouched3 : any;
  focus3 : any;

  public formData: any =  FormGroup;
  Finger = false;

  constructor(
    public formBuilder: FormBuilder,
    public toastr: ToastrService,
    private http: HttpClient,
    private router: Router,
    private notification: NotificationsComponent,
    public bsModalRef: BsModalRef,
    public optionsDevices: ModalOptions,
  ) {}
  ngOnInit(): void {
    this.getData();
    this.formData = this.formBuilder.group({
      entity: ["", [Validators.nullValidator, Validators.required]],
      city: ["", [Validators.nullValidator, Validators.required]],
      role: ["", [Validators.nullValidator, Validators.required]],
    });
  }

  get DataForm() {
    return this.formData.controls;
  }

  getData(): void {
    const Token = 'Token ' + localStorage.getItem('token');
    this.http
      .get(Servers.Deploy + '/api/master/', {
        headers: new HttpHeaders({
          'Content-Type': 'application/json',
          Authorization: Token,
        }),
      })
      .subscribe(
        (response) => {
          var Data: any;
          Data = response;
          console.log(Data);
          this.List = Data;
        },
        (e) => {
          this.notification.showNotification(
            'top',
            'right',
            4,
            'tim-icons icon-simple-remove',
            'Error con comunicación con el servicio. \n' +
              e +
              '. \n Intentalo nuevamente.'
          );
        }
      );
  }

  createData() : void {
    if (!this.formData.invalid) {
      const Token = 'Token ' + localStorage.getItem('token');
      var data = {
        entity: this.formData.value.entity,
        city: this.formData.value.city,
        role: this.formData.value.role
      };

      console.log(data)
  
      this.http
        .post(Servers.Deploy + "/api/master/", data, {
          headers: new HttpHeaders({
            "Content-Type": "application/json",
            Authorization: Token, // Validar atutenticación.
          }),
        })
        .subscribe(
          (response) => {
            this.notification.showNotification(
              "top",
              "right",
              2,
              "tim-icons icon-check-2",
              "Creado!"
            );
            this.getData();
          },
          (e) => {
            this.notification.showNotification(
              "top",
              "right",
              4,
              "tim-icons icon-simple-remove",
              "Se ha presentado un error, intentalo nuevamente."
            );
          }
        );
    }
  }
}
