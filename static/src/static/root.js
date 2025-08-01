/** @odoo-module **/
import { Component} from "@odoo/owl";
import {AlertDialog} from "@web/core/confirmation_dialog/confirmation_dialog";
import {useService} from "@web/core/utils/hooks";
import {Dialog} from "@web/core/dialog/dialog";

export class Root extends Component {
    static template = "test_mobile.Root";
    static components = {Dialog};

    setup() {
        this.dialogService = useService("dialog");
    }

    ShowDialog() {

        console.log("ShowDialog clicked", this.dialogService);
        this.dialogService.add(AlertDialog, {
            body: "This is a working OWL Alert Dialog!",
        });
    }
}