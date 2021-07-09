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
                    <base-input placeholder="First Name"></base-input>
                    <base-input placeholder="Artist/Band Name"></base-input>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <base-input placeholder="Last Name"></base-input>
                </div>
            </div>

            <!-- DATEPICKER -->
            <div class="datepicker-wrapper">
                <date-pickers></date-pickers>
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

export default {
    name: 'bookingForm',
    data() {
        return {
            form: {
                firstName: 'david',
                lastName: 'richter',
                bandName: 'the hecking beatles',
                studio: 'different fur',
                startDate: '2021-07-09',
                endDate: '2021-07-12',
                engineer: 'Randall Dunn',
                costPerHour: '1000',
                estTotalCost: '10000',
            }
        }
    },
    methods: {
        submitForm() {
            console.log('submitForm called')
            axios.post('http://0.0.0.0:8000/booking/submit-booking-data', this.form)
                .then(res => {
                    console.log(res)
                })
                .catch(err => {
                    console.error(err)
                })
        }
    },
    components: {
        DatePickers,
    },
}

</script>

<style>
</style>
