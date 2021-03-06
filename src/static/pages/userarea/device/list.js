import "../../../js/index";
import "../../../scss/components/table.scss";
import PartitialAjax from "django-partitialajax";
import partitial_settings from "django-partitialajax/js/setting";
import setupCrud from "../../../js/crud";

$(function(){

  $("[data-toggle='popover']").popover();
  PartitialAjax.initialize();

  setupCrud(
      PartitialAjax.getPartitialFromElement(document.getElementById("device-list-partitial")),
      PartitialAjax.getPartitialFromElement(document.getElementById("device-create-button")),
      ".device-delete-button"
  );

});