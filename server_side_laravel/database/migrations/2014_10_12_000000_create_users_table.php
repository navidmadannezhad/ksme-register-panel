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
            $table->string('first_name')->nullable();
            $table->string('last_name')->nullable();
            $table->string('email')->unique()->nullable();
            // used for admin
            $table->string('password')->nullable();

            $table->timestamp('email_verified_at')->nullable();
            $table->bigInteger('phone_number')->nullable();
            $table->string('educational_level')->nullable();
            $table->string('educational_field')->nullable();
            $table->string('skills')->nullable();
            $table->string('extra_words')->nullable();
            $table->bigInteger('national_number')->nullable();
            $table->bigInteger('student_number')->nullable();
            $table->string('birthday')->nullable();
            $table->string('corporate_field')->nullable();
            $table->string('activities')->nullable();
            $table->boolean('is_admin')->default(false)->nullable();
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
