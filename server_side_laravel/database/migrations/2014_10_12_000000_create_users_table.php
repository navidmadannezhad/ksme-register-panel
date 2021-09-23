<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('first_name');
            $table->string('last_name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->bigInteger('phone_number');
            $table->string('educational_level');
            $table->string('educational_field');
            $table->string('skills')->nullable();
            $table->string('extra_words')->nullable();
            $table->bigInteger('national_number');
            $table->bigInteger('student_number');
            $table->string('birthday');
            $table->string('corporate_field');
            $table->string('activities')->nullable();
            $table->boolean('activity')->default(false);
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}
