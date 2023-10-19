<script setup lang="ts">
import {computed, reactive, ref} from "vue";
import Input from "./Input.vue";
import Checkbox from "./Checkbox.vue";

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  section: [],
});

const firstNameError = computed(() => {
  if (form.firstName.length < 3) {
    return 'Imię jest za krótkie';
  }

  if (form.firstName.length > 20) {
    return 'Imię jest za długie';
  }

  if (!form.firstName.match(/^\p{L}+$/u)) {
    return 'Imię zawiera niedozwolone znaki';
  }
});

const lastNameError = computed(() => {
  if (form.lastName.length < 3) {
    return 'Nazwisko jest za krótkie';
  }

  if (form.lastName.length > 32) {
    return 'Nazwisko jest za długie';
  }

  if (!form.lastName.match(/^\p{L}+$/u)) {
    return 'Nazwisko zawiera niedozwolone znaki';
  }
});

const emailError = computed(() => {
  if (!form.email.match(/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/)) {
    return 'Niepoprawny adres e-mail';
  }
});

const anyError = computed(() => {
  return !!firstNameError.value || !!lastNameError.value || !!emailError.value;
});

const submitted = ref(false);

function submit() {
  if (anyError.value) return;

  submitted.value = true;
}

</script>

<template>
  <div class="container mx-auto mt-20 flex justify-center">
    <div class="bg-white/20 text-white p-8 rounded-lg max-w-lg w-full">
      <div class="text-center mb-4">
        <a class="inline-block" href="https://akai.org.pl/" target="_blank">
          <img src="../assets/logo.svg" width="64" alt="AKAI"/>
        </a>
        <h1 class="text-3xl font-bold mt-4">Formularz rekrutacyjny</h1>
      </div>

      <div v-if="submitted">
        Cześć <strong>{{ form.firstName }}!</strong> Dziękujemy za wypełnienie formularza rekrutacyjnego. Wkrótce
        skontaktujemy się z Tobą za pomocą podanego adresu e-mail.
      </div>

      <template v-else>
        <div class="grid md:grid-cols-2 gap-4 md:gap-8 mb-4">
          <div>
            <label for="name">Imię</label>
            <Input id="name" v-model="form.firstName" placeholder="Jan"/>
            <small v-if="form.firstName && firstNameError" class="text-primary">{{ firstNameError }}</small>
          </div>
          <div>
            <label for="surname">Nazwisko</label>
            <Input id="surname" v-model="form.lastName" placeholder="Kowalski"/>
            <small v-if="form.lastName && lastNameError" class="text-primary">{{ lastNameError }}</small>
          </div>
        </div>

        <div class="mb-4">
          <label for="email">E-mail</label>
          <Input id="email" v-model="form.email" type="email" placeholder="jankowalski@example.com"/>
          <small v-if="form.email && emailError" class="text-primary">{{ emailError }}</small>
        </div>

        <div class="mb-8">
          <label>Wybierz sekcje, które Cię interesują</label>
          <div class="grid md:grid-cols-2 gap-4 mt-2">
            <Checkbox value="frontend" v-model="form.section">Frontend</Checkbox>
            <Checkbox value="backend" v-model="form.section">Backend</Checkbox>
            <Checkbox value="backend" v-model="form.section">Mobile</Checkbox>
            <Checkbox value="backend" v-model="form.section">Grafika</Checkbox>
          </div>
        </div>

        <div class="text-center">
          <button :disabled="anyError" :class="{'bg-gray-500 text-gray-100': anyError}" @click="submit"
                  class="bg-primary px-12 py-2 rounded font-bold">
            Wyślij
          </button>
        </div>
      </template>
    </div>
  </div>
</template>
