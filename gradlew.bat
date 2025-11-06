@echo off
set DIR=%~dp0
set APP_HOME=%DIR%
set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar;%APP_HOME%\gradle\wrapper\gradle-wrapper-shared.jar;%APP_HOME%\gradle\wrapper\gradle-cli-8.8.jar;%APP_HOME%\gradle\wrapper\gradle-files-8.8.jar;%APP_HOME%\gradle\wrapper\gradle-functional-8.8.jar;%APP_HOME%\gradle\wrapper\gradle-base-annotations-8.8.jar;%APP_HOME%\gradle\wrapper\failureaccess-1.0.1.jar
set DEFAULT_JVM_OPTS=

if not defined JAVA_HOME (
    set JAVA_EXE=java.exe
) else (
    set JAVA_EXE=%JAVA_HOME%\bin\java.exe
)

"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% -Dorg.gradle.appname=%~n0 -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*
