<template>
    <section class="section pb-0 section-components">
        <div class="container mb-5">
          
            <h3 class="h4 text-success font-weight-bold mb-4">Book Studio Time</h3>
            <div class="mb-3">
                <small class="text-uppercase font-weight-bold">About You</small>
            </div>

            <!-- INPUT FIELDS -->
            <div class="row">
                <div class="col-lg-4 col-sm-6">
                    <base-input v-model="form['firstName']" placeholder="First Name"></base-input>
                    <base-input v-model="form['lastName']" placeholder="Last Name"></base-input>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <base-input v-model="form['bandName']" placeholder="Artist/Band Name"></base-input>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <base-input v-model="form['studio']" placeholder="Studio"></base-input>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <base-input v-model="form['engineer']" placeholder="Engineer"></base-input>
                </div>
            </div>

            <!-- DATEPICKER -->
            <div class="row">
                <div class="col-md-4 mt-4 mt-md-0">
                <small class="d-block text-uppercase font-weight-bold mb-3">Pick Some Dates</small>
                <div class="input-daterange datepicker row align-items-center">
                    <div class="col">
                        <base-input addon-left-icon="ni ni-calendar-grid-58">
                        <flat-picker slot-scope="{focus, blur}"
                                        @on-open="focus"
                                        @on-close="blur"
                                        @on-change="onDateChange"
                                        :config="{allowInput: true, mode: 'range',}"
                                        class="form-control datepicker"
                                        v-model="dateRange">
                        </flat-picker>
                        </base-input>
                    </div>
                </div>
                </div>
            </div>
        </div>

        <div class="btn-wrapper">
            <base-button  v-on:click="submitForm"  
                            tag="a"
                            href="#/submit"
                            class="mb-3 mb-sm-0"
                            type="info">
                Submit
            </base-button>
        </div>
    </section>
</template>

<script>

import axios from 'axios'

import DatePickers from './components/JavascriptComponents/DatePickers.vue'
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
    name: 'bookingForm',
    data() {
        return {
            dateRange: '',
            form: {
                firstName: this.firstName,
                lastName: this.lastName,
                bandName: this.bandName,
                studio: this.studio,
                startDate: '',
                endDate: '',
                engineer: this.engineer,
                costPerHour: 1000,
                estTotalCost: 10000,
            }
        }
    },
    methods: {
        submitForm() {
            axios.post('http://0.0.0.0:8000/booking/submit-booking-data', this.form)
                .then(res => {
                    console.log(res)
                })
                .catch(err => {
                    console.error(err)
                })
        },
        onDateChange() {
            const rangeToBook = this.dateRange.split('to')
            if (rangeToBook.length === 2)
                this.form.startDate = rangeToBook[0].trim()
                this.form.endDate = rangeToBook[1].trim()
        }
    },
    components: {
        // DatePickers,
        flatPicker,
    },
}

</script>

<style>
</style>
