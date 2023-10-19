<script setup lang="ts">
const props = defineProps<{
  modelValue?: any[]|boolean,
  value: any,
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: any[]|boolean): void,
}>();

function checked(event: Event) {
  let isChecked = event.target?.checked as boolean
  if (props.modelValue instanceof Array) {
    let newValue = [...props.modelValue]
    if (isChecked) {
      newValue.push(props.value)
    } else {
      newValue.splice(newValue.indexOf(props.value), 1)
    }
    emit('update:modelValue', newValue)
  } else {
    emit('update:modelValue', isChecked)
  }
}
</script>

<template>
  <label class="block relative cursor-pointer">
    <input @change="checked" type="checkbox" class="absolute w-full h-full left-0 top-0 -z-10 opacity-0"/>
    <div
        class="border-2 rounded border-primary text-primary text-center font-bold select-none p-4 transition-colors">
      <slot/>
    </div>
  </label>
</template>

<style scoped>
input[type="checkbox"]:checked + div {
  @apply text-white bg-primary;
}
</style>
