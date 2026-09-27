################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/function/auto_corr.c \
../Core/Src/function/debugs.c \
../Core/Src/function/f_set.c \
../Core/Src/function/func_sel.c \
../Core/Src/function/general_func.c \
../Core/Src/function/measure.c \
../Core/Src/function/midi.c \
../Core/Src/function/synth.c \
../Core/Src/function/usb.c 

OBJS += \
./Core/Src/function/auto_corr.o \
./Core/Src/function/debugs.o \
./Core/Src/function/f_set.o \
./Core/Src/function/func_sel.o \
./Core/Src/function/general_func.o \
./Core/Src/function/measure.o \
./Core/Src/function/midi.o \
./Core/Src/function/synth.o \
./Core/Src/function/usb.o 

C_DEPS += \
./Core/Src/function/auto_corr.d \
./Core/Src/function/debugs.d \
./Core/Src/function/f_set.d \
./Core/Src/function/func_sel.d \
./Core/Src/function/general_func.d \
./Core/Src/function/measure.d \
./Core/Src/function/midi.d \
./Core/Src/function/synth.d \
./Core/Src/function/usb.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/function/%.o Core/Src/function/%.su Core/Src/function/%.cyclo: ../Core/Src/function/%.c Core/Src/function/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F411xE -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../USB_DEVICE/App -I../USB_DEVICE/Target -I../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -I../Middlewares/ST/STM32_USB_Device_Library/Class/HID/Inc -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-function

clean-Core-2f-Src-2f-function:
	-$(RM) ./Core/Src/function/auto_corr.cyclo ./Core/Src/function/auto_corr.d ./Core/Src/function/auto_corr.o ./Core/Src/function/auto_corr.su ./Core/Src/function/debugs.cyclo ./Core/Src/function/debugs.d ./Core/Src/function/debugs.o ./Core/Src/function/debugs.su ./Core/Src/function/f_set.cyclo ./Core/Src/function/f_set.d ./Core/Src/function/f_set.o ./Core/Src/function/f_set.su ./Core/Src/function/func_sel.cyclo ./Core/Src/function/func_sel.d ./Core/Src/function/func_sel.o ./Core/Src/function/func_sel.su ./Core/Src/function/general_func.cyclo ./Core/Src/function/general_func.d ./Core/Src/function/general_func.o ./Core/Src/function/general_func.su ./Core/Src/function/measure.cyclo ./Core/Src/function/measure.d ./Core/Src/function/measure.o ./Core/Src/function/measure.su ./Core/Src/function/midi.cyclo ./Core/Src/function/midi.d ./Core/Src/function/midi.o ./Core/Src/function/midi.su ./Core/Src/function/synth.cyclo ./Core/Src/function/synth.d ./Core/Src/function/synth.o ./Core/Src/function/synth.su ./Core/Src/function/usb.cyclo ./Core/Src/function/usb.d ./Core/Src/function/usb.o ./Core/Src/function/usb.su

.PHONY: clean-Core-2f-Src-2f-function

