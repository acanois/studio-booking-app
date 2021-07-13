<template>
  <section class="section pb-0 section-components">
    <div class="container mb-5">
      <h3 class="h4 text-success font-weight-bold mb-4">Booking Confirmation</h3>

      <div class="row" style="text-align: left;">
        <div class="col-lg-4 col-sm-6">
          <div class="mb-5">
            <small class="text-uppercase font-weight-bold">Name</small>
            <br>
            {{ firstName }} {{ lastName }}
          </div>
        </div>
        <div class="col-lg-4 col-sm-6">
          <div class="mb-5">
            <small class="text-uppercase font-weight-bold">Artist Name</small>
            <br>
            {{ bandName }}
          </div>
        </div>
      </div>

      <div class="row" style="text-align: left;">
        <div class="col-lg-4 col-sm-6">
          <div class="mb-5">
            <small class="text-uppercase font-weight-bold">Dates</small>
            <br>
            {{ startDate }} to {{ endDate }}
          </div>
        </div>
        <div class="col-lg-4 col-sm-6">
          <div class="mb-5">
            <small class="text-uppercase font-weight-bold">Engineer</small>
            <br>
            {{ engineer }}
          </div>
        </div>
      </div>

      <div class="row" style="text-align: left;">
        <div class="col-lg-4 col-sm-6">
          <div class="mb-5">
            <small class="text-uppercase font-weight-bold">Studio</small>
            <br>
            {{ studio }}
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'bookingConfirmation',
  data() {
    return {
      pk: 5,
      firstName: '',
      lastName: '',
      bandName: '',
      startDate: '',
      endDate: '',
    }
  },
  mounted() {
    axios
      .get('http://localhost:8000/booking/get-one-booking', this.confirmationData)
      .then(res => {
        this.firstName = res.data.first_name
        this.lastName = res.data.last_name
        this.bandName = res.data.band_name
        this.startDate = res.data.start_date
        this.endDate = res.data.end_date
        this.engineer = res.data.engineer
        this.studio = res.data.studio
      })
      .then(console.log('NEXT'))
      .catch(err => console.log(err))
  }
}
</script>