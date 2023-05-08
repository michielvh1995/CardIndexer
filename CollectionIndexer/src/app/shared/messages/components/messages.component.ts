import { Component } from '@angular/core';
import { MessageService } from '../services/message.service';

@Component({
  selector: 'app-messages',
  templateUrl: '../pages/messages.component.html',
  styleUrls: ['../pages/messages.component.css']
})
export class MessagesComponent {
  constructor(public messageService: MessageService) {}
}
