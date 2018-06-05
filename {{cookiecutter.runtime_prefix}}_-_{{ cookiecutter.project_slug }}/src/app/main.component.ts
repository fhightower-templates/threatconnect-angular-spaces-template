import {
    Component,
    OnInit
} from '@angular/core';

import { Router } from '@angular/router';

import {
    SpacesBaseService,
    SpacesLoggingService,
    SpacesMessagesService,
} from 'spaces-ng/';

{% if cookiecutter.use_zurb_foundation == 'y' %}declare var $:any{% endif %}

@Component({
    templateUrl: './main.component.html',
    selector: 'tc-main',
})
export class MainComponent implements OnInit {
    constructor(
        private logging: SpacesLoggingService,
        private messages: SpacesMessagesService,
        private router: Router,
        private spacesBase: SpacesBaseService
    ) {
        this.logging.moduleColor('#FFFF00', '#000', 'MainComponent');  // set logging console colors
    }

    ngOnInit() {
        this.messages.showSuccess('Success Message', 'This is the start of something great!');
        {% if cookiecutter.use_zurb_foundation == 'y' %}$(document).foundation();{% endif %}
    }
         
    goTo(routePath: string) {
        this.router.navigate([routePath]);
    }
}
