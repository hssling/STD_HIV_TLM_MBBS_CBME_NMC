#!/usr/bin/env sh

APP_BASE_NAME=`basename "$0"`
APP_HOME=`cd "$(dirname "$0")"; pwd -P`
CLASSPATH="$APP_HOME/gradle/wrapper/gradle-wrapper.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/gradle-wrapper-shared.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/gradle-cli-8.8.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/gradle-files-8.8.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/gradle-functional-8.8.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/gradle-base-annotations-8.8.jar"
CLASSPATH="$CLASSPATH:$APP_HOME/gradle/wrapper/failureaccess-1.0.1.jar"
DEFAULT_JVM_OPTS=""

if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/bin/java" ] ; then
        JAVACMD="$JAVA_HOME/bin/java"
    else
        echo "ERROR: JAVA_HOME is set to an invalid directory" >&2
        exit 1
    fi
else
    JAVACMD="java"
fi

exec "$JAVACMD" $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS \
    -Dorg.gradle.appname=$APP_BASE_NAME \
    -classpath "$CLASSPATH" \
    org.gradle.wrapper.GradleWrapperMain "$@"
