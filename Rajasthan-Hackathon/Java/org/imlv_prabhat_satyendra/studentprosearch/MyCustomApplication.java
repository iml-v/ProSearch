package org.imlv_prabhat_satyendra.studentprosearch;

import android.app.Application;

import com.androidnetworking.AndroidNetworking;

/**
 * Created by IMLV on 27-11-2017.
 */

public class MyCustomApplication extends Application {
    @Override
    public void onCreate(){
        super.onCreate();
        AndroidNetworking.initialize(getApplicationContext());

    }


}
