<template>
  <div class="row">
    <div class="col-md-4 mt-4 mt-md-0">
      <small class="d-block text-uppercase font-weight-bold mb-3">Pick Some Dates</small>
      <div class="input-daterange datepicker row align-items-center">
        <div class="col">
            <base-input addon-left-icon="ni ni-calendar-grid-58">
              <flat-picker slot-scope="{focus, blur}"
                            @on-open="focus"
                            @on-close="blur"
                            :config="{allowInput: true, mode: 'range',}"
                            class="form-control datepicker"
                            v-model="dates.range">
              </flat-picker>
            </base-input>
          </div>
      </div>
    </div>
  </div>
</template>
<script>
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
export default {
  components: {
    flatPicker
  },
  data() {
    return {
      dates: {
        simple: "2021-07-17",
        range: "2021-07-17 to 2021-07-19"
      }
    };
  }
};
</script>
