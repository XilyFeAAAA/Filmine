<template>
    <div class="store" @click="isMenuVisible = false">
        <div class="normal" v-show="!method">
            <div class="stack dock">
                <div class="input-container">
                    <span>
                        <svg
                            class="with-icon_icon__aLCKg"
                            data-testid="geist-icon"
                            fill="none"
                            height="24"
                            shape-rendering="geometricPrecision"
                            stroke="currentColor"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="1.5"
                            viewBox="0 0 24 24"
                            width="24"
                            style="color: currentcolor; width: 20px; height: 20px"
                        >
                            <path d="M11 17.25a6.25 6.25 0 110-12.5 6.25 6.25 0 010 12.5z"></path>
                            <path d="M16 16l4.5 4.5"></path>
                        </svg>
                    </span>
                    <input type="text" placeholder="Search" />
                </div>
                <div class="switch-container">
                    <button :class="{ active: align === 'grid' }" @click="align = 'grid'">
                        <span
                            ><svg
                                class="with-icon_icon__aLCKg"
                                data-testid="geist-icon"
                                fill="none"
                                height="24"
                                shape-rendering="geometricPrecision"
                                stroke="currentColor"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.5"
                                viewBox="0 0 24 24"
                                width="24"
                                style="
                                    color: currentcolor;
                                    vertical-align: text-top;
                                    width: 18px;
                                    height: 18px;
                                "
                            >
                                <path d="M3 3h7v7H3z"></path>
                                <path d="M14 3h7v7h-7z"></path>
                                <path d="M14 14h7v7h-7z"></path>
                                <path d="M3 14h7v7H3z"></path></svg
                        ></span>
                    </button>
                    <button :class="{ active: align === 'row' }" @click="align = 'row'">
                        <span
                            ><svg
                                class="with-icon_icon__aLCKg"
                                data-testid="geist-icon"
                                fill="none"
                                height="24"
                                shape-rendering="geometricPrecision"
                                stroke="currentColor"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.5"
                                viewBox="0 0 24 24"
                                width="24"
                                style="
                                    color: currentcolor;
                                    vertical-align: text-top;
                                    width: 18px;
                                    height: 18px;
                                "
                            >
                                <path d="M8 6h13"></path>
                                <path d="M8 12h13"></path>
                                <path d="M8 18h13"></path>
                                <path d="M3 6h.01"></path>
                                <path d="M3 12h.01"></path>
                                <path d="M3 18h.01"></path></svg
                        ></span>
                    </button>
                </div>
                <button
                    class="menu-btn"
                    @click.stop="isMenuVisible = !isMenuVisible"
                    ref="menuButton"
                >
                    <span style="margin-right: 5px">Add New</span>
                    <span><font-awesome-icon :icon="['fas', 'chevron-down']" /></span>
                </button>
            </div>
            <div class="stack projects-grid" v-show="align === 'grid'">
                <div
                    class="project-card"
                    v-for="(project, idx) in projects"
                    :key="idx"
                    @click="$router.push({ path: `/store/data/${project.token}` })"
                >
                    <div class="card-row">
                        <div class="title">
                            <img src="https://img1.doubanio.com/favicon.ico" />
                            <div>
                                <p>Xilyfe</p>
                                <p>douban - {{ project.token }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="card-row">Douban</div>
                    <div class="card-row">{{ project.created_time }}</div>
                    <a
                        class="card-share"
                        @click="$router.push({ path: `/store/edit/${project.token}` })"
                    >
                        <span>
                            <font-awesome-icon icon="arrow-up-right-from-square" />
                        </span>
                    </a>
                </div>
            </div>
            <div class="stack projects-row" v-show="align === 'row'">
                <div class="project-row" v-for="(project, idx) in projects" :key="idx">
                    <div class="row-container">
                        <div class="l-part">
                            <div class="avatar">
                                <span>
                                    <img src="https://img1.doubanio.com/favicon.ico" />
                                </span>
                            </div>
                            <div class="content">
                                <p class="underline">Xilyfe</p>
                                <p class="underline">
                                    douban - {{ project.token }}
                                    <span class="share-svg"
                                        ><svg
                                            data-v-24bb8976=""
                                            aria-hidden="true"
                                            focusable="false"
                                            data-prefix="fas"
                                            data-icon="arrow-up-right-from-square"
                                            role="img"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 512 512"
                                            class="svg-inline--fa fa-arrow-up-right-from-square"
                                        >
                                            <path
                                                data-v-24bb8976=""
                                                fill="currentColor"
                                                d="M320 0c-17.7 0-32 14.3-32 32s14.3 32 32 32h82.7L201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L448 109.3V192c0 17.7 14.3 32 32 32s32-14.3 32-32V32c0-17.7-14.3-32-32-32H320zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"
                                                class=""
                                            ></path></svg
                                    ></span>
                                </p>
                            </div>
                        </div>
                        <div class="r-part">
                            <p class="underline">Douban</p>
                            <p>{{ project.created_time }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="alter" v-show="method">
            <div class="header">
                <div class="header-title">
                    <div class="header-title-left">
                        <h1>Douban</h1>
                    </div>
                    <div class="header-title-right">
                        <button class="btn-item-1">Git Respository</button>
                        <button class="btn-item-1">Domains</button>
                        <button class="btn-item-1">Visit</button>
                    </div>
                </div>
            </div>
            <div class="dashboard">
                <div class="dashboard-card-wrapper">
                    <div class="back-tag" @click="$router.push({ path: '/store' })">
                        <div>
                            <font-awesome-icon
                                style="margin-right: 5px; width: 12px; height: 12px"
                                :icon="['fas', 'arrow-left']"
                            />
                            <span style="font-size: 0.875rem; font-weight: 400">Back</span>
                        </div>
                    </div>
                    <div class="dashboard-card-header">
                        <div class="dashboard-card-header-title">Project Deployment</div>
                        <p>The deployment that is available to your friends.</p>
                    </div>
                    <div class="dashboard-wrapper" v-show="method !== 'add'">
                        <div class="dashboard-card">
                            <div class="fieldset-content">
                                <div class="screenshot">
                                    <img src="./screenshot.png" alt="" />
                                </div>
                                <div class="dashboard-meta">
                                    <div class="meta-row">
                                        <h3>DEPLOYMENT</h3>
                                        <p>{{ current_project.name }}</p>
                                    </div>
                                    <div class="meta-row">
                                        <h3>DOMAINS</h3>
                                        <p>{{ current_project.source }}</p>
                                    </div>
                                    <div class="meta-row">
                                        <h3>STATUS</h3>
                                        <p>Ready</p>
                                    </div>
                                    <div class="meta-row">
                                        <h3>Note</h3>
                                        <p>{{ current_project.notes }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="configure-content" v-show="method === 'edit'">
                                <div class="configure-title">
                                    <h2>Configure Project</h2>
                                </div>
                                <hr />
                                <div class="configure-setting">
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Name</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <input type="text" />
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Source</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <select>
                                                <option value="">Douban</option>
                                                <option value="">NetFlix</option>
                                                <option value="">Tmdb</option>
                                                <option value="">Apple TV</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Notes</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <textarea></textarea>
                                        </div>
                                    </div>
                                    <div class="setting-block">
                                        <details>
                                            <summary>Source Account Settings</summary>
                                            <div>
                                                <div class="account-block" style="width: 100%">
                                                    <div class="account-block-title">
                                                        <p>Account Cookies</p>
                                                        <span
                                                            class="tooltip_container__8oRxQ"
                                                            data-testid="legacy/tooltip-trigger"
                                                            data-version="v1"
                                                            tabindex="0"
                                                            ><svg
                                                                class="with-icon_icon__aLCKg"
                                                                data-testid="geist-icon"
                                                                fill="none"
                                                                height="24"
                                                                shape-rendering="geometricPrecision"
                                                                stroke="currentColor"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                                stroke-width="1.5"
                                                                viewBox="0 0 24 24"
                                                                width="24"
                                                                style="
                                                                    color: var(--accents-3);
                                                                    width: 15px;
                                                                    height: 15px;
                                                                "
                                                            >
                                                                <path
                                                                    d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                                                                ></path>
                                                                <path
                                                                    d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"
                                                                ></path>
                                                                <circle
                                                                    cx="12"
                                                                    cy="17"
                                                                    r=".5"
                                                                ></circle></svg
                                                        ></span>
                                                    </div>
                                                    <div class="account-block-content">
                                                        <input
                                                            type="text"
                                                            :class="{ disabled: !input_state[0] }"
                                                            :disabled="!input_state[0]"
                                                        />
                                                        <toggle
                                                            :text="toggle_text"
                                                            :val.sync="input_state[0]"
                                                        />
                                                    </div>
                                                </div>
                                                <div class="account-block" style="width: 100%">
                                                    <div class="account-block-title">
                                                        <p>Login Authorization</p>
                                                        <span
                                                            class="tooltip_container__8oRxQ"
                                                            data-testid="legacy/tooltip-trigger"
                                                            data-version="v1"
                                                            tabindex="0"
                                                            ><svg
                                                                class="with-icon_icon__aLCKg"
                                                                data-testid="geist-icon"
                                                                fill="none"
                                                                height="24"
                                                                shape-rendering="geometricPrecision"
                                                                stroke="currentColor"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                                stroke-width="1.5"
                                                                viewBox="0 0 24 24"
                                                                width="24"
                                                                style="
                                                                    color: var(--accents-3);
                                                                    width: 15px;
                                                                    height: 15px;
                                                                "
                                                            >
                                                                <path
                                                                    d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                                                                ></path>
                                                                <path
                                                                    d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"
                                                                ></path>
                                                                <circle
                                                                    cx="12"
                                                                    cy="17"
                                                                    r=".5"
                                                                ></circle></svg
                                                        ></span>
                                                    </div>
                                                    <div class="account-block-content"></div>
                                                </div>
                                            </div>
                                        </details>
                                    </div>
                                    <div class="setting-block">
                                        <details>
                                            <summary>Message Delivery Settings</summary>
                                            <div>
                                                <div class="account-block" style="width: 100%">
                                                    <div class="account-block-title">
                                                        <p>Account Cookies</p>
                                                        <span
                                                            class="tooltip_container__8oRxQ"
                                                            data-testid="legacy/tooltip-trigger"
                                                            data-version="v1"
                                                            tabindex="0"
                                                            ><svg
                                                                class="with-icon_icon__aLCKg"
                                                                data-testid="geist-icon"
                                                                fill="none"
                                                                height="24"
                                                                shape-rendering="geometricPrecision"
                                                                stroke="currentColor"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                                stroke-width="1.5"
                                                                viewBox="0 0 24 24"
                                                                width="24"
                                                                style="
                                                                    color: var(--accents-3);
                                                                    width: 15px;
                                                                    height: 15px;
                                                                "
                                                            >
                                                                <path
                                                                    d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                                                                ></path>
                                                                <path
                                                                    d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"
                                                                ></path>
                                                                <circle
                                                                    cx="12"
                                                                    cy="17"
                                                                    r=".5"
                                                                ></circle></svg
                                                        ></span>
                                                    </div>
                                                    <div class="account-block-content">
                                                        <input
                                                            type="text"
                                                            :class="{ disabled: !input_state[0] }"
                                                            :disabled="!input_state[0]"
                                                        />
                                                        <toggle
                                                            :text="toggle_text"
                                                            :val.sync="input_state[0]"
                                                        />
                                                    </div>
                                                </div>
                                            </div>
                                        </details>
                                    </div>
                                </div>
                            </div>
                            <div class="configure-content" v-show="method === 'data'">
                                <div class="configure-title">
                                    <h2>观影可视化数据展示</h2>
                                </div>
                                <hr />

                                <div v-if="echart_data">
                                    <div class="configure-title">
                                        <h2>词云 WordCloud</h2>
                                    </div>
                                    <div
                                        style="
                                            position: relative;
                                            width: 100%;
                                            display: flex;
                                            justify-content: center;
                                        "
                                    >
                                        <wordcloud
                                            :data="echart_data.word"
                                            style="width: 50%; height: 400px"
                                        />
                                    </div>
                                    <div class="configure-title">
                                        <h2>观影类型 Genre</h2>
                                    </div>
                                    <div style="position: relative; width: 100%; display: flex">
                                        <barchart :data="echart_data.genre" />
                                        <piechart :data="echart_data.genre" />
                                    </div>
                                    <div class="configure-title">
                                        <h2>观影来源 Region</h2>
                                    </div>
                                    <div style="position: relative; width: 100%; display: flex">
                                        <barchart :data="echart_data.country" />
                                        <piechart :data="echart_data.country" />
                                    </div>
                                    <div class="configure-title">
                                        <h2>观影年代 Year</h2>
                                    </div>
                                    <div style="position: relative; width: 100%; display: flex">
                                        <barchart :data="echart_data.year" />
                                        <piechart :data="echart_data.year" />
                                    </div>
                                    <div style="position: relative; width: 100%; display: flex">
                                        <barchart :data="echart_data.duration" />
                                        <barchart :data="echart_data.rating" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="dashboard-wrapper" v-show="method === 'add'">
                        <div class="dashboard-card">
                            <div class="configure-content">
                                <div class="configure-title">
                                    <h2>Configure Project</h2>
                                </div>
                                <hr />
                                <div class="configure-setting">
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Name</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <input type="text" v-model="deploy_info.name" />
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Source</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <select v-model="deploy_info.source">
                                                <option value="Douban">Douban</option>
                                                <option value="NetFlix">NetFlix</option>
                                                <option value="Tmdb">Tmdb</option>
                                                <option value="AppleTv">Apple TV</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Project Notes</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <textarea v-model="deploy_info.notes"></textarea>
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Push Email</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <div class="account-block-content">
                                                <input
                                                    type="text"
                                                    v-model="deploy_info.email"
                                                    :class="{ disabled: !input_state[0] }"
                                                    :disabled="!input_state[0]"
                                                />
                                                <toggle
                                                    :text="toggle_text"
                                                    :val.sync="input_state[0]"
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="setting-row">
                                        <div class="setting-row-title">
                                            <h4>Account Cookies</h4>
                                        </div>
                                        <div class="setting-row-content">
                                            <div class="account-block-content">
                                                <input
                                                    type="text"
                                                    v-model="deploy_info.cookie"
                                                    :class="{ disabled: !input_state[1] }"
                                                    :disabled="!input_state[1]"
                                                />
                                                <toggle
                                                    :text="toggle_text"
                                                    :val.sync="input_state[1]"
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="qrcode" v-show="deployed" style="margin-top: 1rem">
                                        <div class="setting-block">
                                            <details open>
                                                <summary>Account Settings</summary>
                                                <div>
                                                    <div class="account-block" style="width: 100%">
                                                        <div class="account-block-title">
                                                            <p>QRcode</p>
                                                            <span
                                                                class="tooltip_container__8oRxQ"
                                                                data-testid="legacy/tooltip-trigger"
                                                                data-version="v1"
                                                                tabindex="0"
                                                                ><svg
                                                                    class="with-icon_icon__aLCKg"
                                                                    data-testid="geist-icon"
                                                                    fill="none"
                                                                    height="24"
                                                                    shape-rendering="geometricPrecision"
                                                                    stroke="currentColor"
                                                                    stroke-linecap="round"
                                                                    stroke-linejoin="round"
                                                                    stroke-width="1.5"
                                                                    viewBox="0 0 24 24"
                                                                    width="24"
                                                                    style="
                                                                        color: var(--accents-3);
                                                                        width: 15px;
                                                                        height: 15px;
                                                                    "
                                                                >
                                                                    <path
                                                                        d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                                                                    ></path>
                                                                    <path
                                                                        d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"
                                                                    ></path>
                                                                    <circle
                                                                        cx="12"
                                                                        cy="17"
                                                                        r=".5"
                                                                    ></circle></svg
                                                            ></span>
                                                        </div>
                                                        <div
                                                            class="account-block-content"
                                                            style="justify-content: center"
                                                        >
                                                            <img :src="qrcode_url" alt="" />
                                                        </div>
                                                    </div>
                                                </div>
                                            </details>
                                        </div>
                                    </div>
                                    <button
                                        class="btn-item-2"
                                        :disabled="deployed"
                                        style="width: 100%"
                                        @click="deployProject"
                                    >
                                        <span style="font-size: 14px; font-weight: 500"
                                            >Deploy</span
                                        >
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="dashboard-card">
                            <div class="configure-content">
                                <div class="configure-title">
                                    <h2>Deploy</h2>
                                </div>
                                <hr />
                                <p style="font-weight: 400; color: #999; font-size: 14px">
                                    Preparing deployment
                                </p>
                                <div style="margin-top: 1rem">
                                    <div class="deploy-step">
                                        <div class="step-row">
                                            <font-awesome-icon
                                                :icon="['fa', 'chevron-right']"
                                                style="margin-right: 1rem"
                                            />
                                            Building
                                        </div>
                                        <div
                                            class="spinner"
                                            :class="
                                                progress >= 0
                                                    ? progress === 0
                                                        ? 'run'
                                                        : 'over'
                                                    : ''
                                            "
                                        ></div>
                                    </div>
                                    <div class="deploy-step">
                                        <div class="step-row">
                                            <font-awesome-icon
                                                :icon="['fa', 'chevron-right']"
                                                style="margin-right: 1rem"
                                            />
                                            Collecting Infomations
                                        </div>
                                        <div
                                            class="spinner"
                                            :class="
                                                progress >= 1
                                                    ? progress === 1
                                                        ? 'run'
                                                        : 'over'
                                                    : ''
                                            "
                                        ></div>
                                    </div>
                                    <div class="deploy-step">
                                        <div class="step-row">
                                            <font-awesome-icon
                                                :icon="['fa', 'chevron-right']"
                                                style="margin-right: 1rem"
                                            />
                                            Collect Movies
                                        </div>
                                        <div
                                            class="spinner"
                                            :class="
                                                progress >= 2
                                                    ? progress === 2
                                                        ? 'run'
                                                        : 'over'
                                                    : ''
                                            "
                                        ></div>
                                    </div>
                                    <div class="deploy-step">
                                        <div class="step-row">
                                            <font-awesome-icon
                                                :icon="['fa', 'chevron-right']"
                                                style="margin-right: 1rem"
                                            />
                                            Saving
                                        </div>
                                        <div
                                            class="spinner"
                                            :class="
                                                progress >= 3
                                                    ? progress === 3
                                                        ? 'run'
                                                        : 'over'
                                                    : ''
                                            "
                                        ></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div
            class="menu-wrapper"
            :class="{ active: isMenuVisible }"
            :style="{ top: menuTop, left: menuLeft }"
        >
            <ul>
                <li @click="$router.push({ path: '/store/add' })">Project</li>
                <li>Domain</li>
                <li>Storage</li>
                <li>Team</li>
            </ul>
        </div>
    </div>
</template>
<script>
import wordcloud from '@/components/echart/wordcloud.vue'
import barchart from '@/components/echart/bar-chart.vue'
import piechart from '@/components/echart/pie-chart.vue'
import toggle from '@/components/toggle.vue'
import axios from 'axios'
export default {
    props: {
        method: String,
        token: String,
    },
    components: {
        toggle,
        wordcloud,
        barchart,
        piechart,
    },
    data() {
        return {
            add_token: '',
            align: 'grid',
            toggle_text: 'OVERRIDE',
            isMenuVisible: false,
            isFixed: false,
            input_state: [false],
            deployed: false,
            qrcode_url: '',
            deploy_info: {
                name: '',
                source: 'Douban',
                notes: '',
                cookie: '',
                email: '',
            },
            progress: 0,
            projects: [],
            current_project: {},
            visual_data: {},
        }
    },
    computed: {
        echart_data() {
            if (this.visual_data) {
                const newData = {}
                Object.keys(this.visual_data).forEach((key) => {
                    newData[key] = Object.keys(this.visual_data[key]).map((name) => ({
                        name,
                        value: this.visual_data[key][name],
                    }))
                })
                return newData
            } else return {}
        },
        menuTop() {
            if (this.isMenuVisible && this.$refs.menuButton) {
                return (
                    this.$refs.menuButton.offsetTop + this.$refs.menuButton.offsetHeight + 10 + 'px'
                )
            } else {
                return false
            }
        },
        menuLeft() {
            if (this.isMenuVisible && this.$refs.menuButton) {
                return this.$refs.menuButton.offsetLeft + 'px'
            } else {
                return false
            }
        },
    },
    mounted() {
        if (this.$route.query.arrangement) this.align = this.$route.query.arrangement
        if (this.method === 'add') this.addProject()
        else if (this.method === 'edit') {
            if (this.token === undefined) {
                alert('项目token错误')
                this.$router.push({ path: '/store' })
            }
            // 获取这个token的project的数据
        } else if (this.method === 'data') {
            this.getProject()
            this.getMovieStats()
        } else this.getStore()
    },
    watch: {
        method(newVal) {
            if (newVal === 'data') {
                this.getProject()
                this.getMovieStats()
            } else if (newVal === 'add') this.addProject()
            else if (newVal === 'edit') alert('edit')
            else this.getStore()
        },
    },
    methods: {
        getStore() {
            axios
                .get(this.$api.INTERFACES.getStoretAPI, {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: localStorage.getItem('token'),
                    },
                })
                .then((response) => {
                    if (response.data.code === 200) {
                        this.projects = response.data.data.storeInfo
                    } else {
                        alert(response.data.err_msg)
                    }
                })
                .catch((error) => {
                    alert('获取项目失败，请重新登陆')
                })
        },
        addProject() {
            axios
                .get(this.$api.INTERFACES.addProjectAPI, {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: localStorage.getItem('token'),
                    },
                })
                .then((response) => {
                    if (response.data.code === 200) {
                        this.add_token = response.data.data.token
                    } else {
                        alert('创建项目失败，请重新登陆')
                    }
                })
                .catch((error) => {
                    alert('创建项目失败，请重新登陆')
                })
        },
        getMovieStats() {
            axios
                .get(this.$api.INTERFACES.getMovieStatsAPI + `/${this.token}`, {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: localStorage.getItem('token'),
                    },
                })
                .then((response) => {
                    if (response.data.code === 200) {
                        this.visual_data = response.data.data.stats
                    } else {
                        alert('获取项目可视化信息错误,请重新登陆')
                    }
                })
                .catch((error) => {
                    alert(error)
                })
        },
        getProject() {
            axios
                .get(this.$api.INTERFACES.getProjectAPI + `/${this.token}`, {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: localStorage.getItem('token'),
                    },
                })
                .then((response) => {
                    if (response.data.code === 200) {
                        this.current_project = response.data.data.project
                    } else {
                        alert('获取项目信息，请重新登陆')
                    }
                })
                .catch((error) => {
                    alert('创建项目失败，请重新登陆')
                })
        },
        deployProject() {
            axios
                .post(
                    this.$api.INTERFACES.deployProjectAPI,
                    {
                        new_deploy_info: this.deploy_info,
                        token: this.add_token,
                    },
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: localStorage.getItem('token'),
                        },
                    },
                )
                .then((response) => {
                    if (response.data.code === 200) {
                        this.getQrcode()
                    } else {
                        alert('部署项目失败，请重新登陆')
                    }
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        getQrcode() {
            let times = 5
            let queryTimerId = setInterval(() => {
                console.log(`轮询第${5 - times}次`)
                axios
                    .get(this.$api.INTERFACES.qrcodeAPI + `/${this.add_token}`, {
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: localStorage.getItem('token'),
                        },
                    })
                    .then((response) => {
                        if (response.data.code === 200) {
                            clearInterval(queryTimerId)
                            console.log(response.data)
                            this.qrcode_url = response.data.data.url
                            this.deployed = true
                            this.getProgress()
                        } else {
                            times--
                            if (times === 0) clearInterval(queryTimerId)
                        }
                    })
                    .catch((error) => {
                        clearInterval(queryTimerId)
                    })
            }, 3000)
        },
        getProgress() {
            let queryTimerId = setInterval(() => {
                console.log(`轮询状态`)
                axios
                    .get(this.$api.INTERFACES.stateAPI + `/${this.add_token}`, {
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: localStorage.getItem('token'),
                        },
                    })
                    .then((response) => {
                        if (response.data.code === 200) {
                            console.log(response.data)
                            this.progress = response.data.data.progress
                            if (this.progress === 4) {
                                clearInterval(queryTimerId)
                                setTimeout(() => {
                                    this.$router.push({ path: '/store' })
                                }, 5000)
                            }
                        } else {
                            clearInterval(queryTimerId)
                        }
                    })
                    .catch((error) => {
                        clearInterval(queryTimerId)
                        alert('轮询出错')
                    })
            }, 3000)
        },
    },
}
</script>
<style scoped>
.back-tag {
    position: absolute;
    /* left: 10px; */
    top: 10px;
    cursor: pointer;
}

.store {
    position: relative;
    height: 100%;
    overflow: hidden;
}

.store .normal {
    display: flex;
    flex-direction: column;
    align-items: center;

    width: 100%;
    padding-top: 5vh;
}

.store .stack {
    width: 100%;
    max-width: 75vw;
    margin: 10px 0;
}

.dock {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    justify-content: flex-start;
    flex: initial;
    gap: 8px;
}

.dock .input-container {
    display: flex;
    align-items: center;
    width: 100%;
    max-width: 100%;
    font-style: 0.875rem;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    transition: border-color 0.15s ease;
}

.dock .input-container span {
    position: relative;
    display: flex;
    align-items: center;
    height: 40px;
    padding: 0 12px;
    color: #888;
    border-right: 0;
    flex-shrink: 0;
    margin-right: -12px;
    background-color: #fff;
}

.dock .input-container input {
    display: inline-flex;
    font-size: 14px;
    height: 40px;
    width: 100%;
    min-width: 0;
    padding: 0 12px;
    background: #fff;
    color: #888;
    order: 1;
    outline: none;
    -webkit-tap-highlight-color: transparent;
}

.dock .input-container input:focus ~ .input-container {
    border-color: #000;
}

.dock .switch-container {
    position: relative;
    display: flex;
    align-items: center;
    padding: 3px;
    background: #fff;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    max-width: 100%;
    height: 40px;
    font-size: 0.875rem;
    -webkit-user-select: none;
    user-select: none;
}

.dock .switch-container button {
    width: 40px;
    height: 32px;
    color: #888;
    border-radius: 5px;
    background-color: #fff;
}

.dock .switch-container button:hover {
    color: #000;
}

.dock .switch-container button.active {
    color: #000;
    background-color: #eaeaea;
}

.dock .menu-btn {
    padding: 0 12px;
    height: 40px;
    min-width: 128px;
    max-width: 128px;
    font-style: 0.875rem;
    font-weight: 500;
    border: 1px solid #000;
    border-radius: 5px;
    color: #fff;
    background-color: #000;
    transition: all 0.15s;
}

.dock .menu-btn:hover {
    color: #000;
    background-color: #fff;
}

.projects-grid {
    display: grid;
    grid-gap: 24px;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
}

.projects-grid .project-card {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 24px;
    background: #fff;
    border-radius: 8px;
    min-width: 350px;
    height: 100%;
    border: 1px solid #eaeaea;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
    cursor: pointer;
    user-select: none;
    transition: box-shadow 0.15s ease;
}

.projects-grid .project-card:hover {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.card-share {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    right: 0;
    top: 0;
    width: 32px;
    height: 32px;
    color: #fff;
    border: 1px solid #000;
    border-radius: 50%;
    background-color: #000;
    transform: translate(35%, 0);
    font-size: 0.875rem;
    opacity: 0;
    pointer-events: none;
    transition: 0.15s ease;
    transition-property: opacity, transform;
    cursor: pointer;
}

.card-share:hover {
    background-color: #fff;
    color: #000;
}
.project-card:hover .card-share {
    opacity: 1;
    pointer-events: auto;
    transform: translate(35%, -30%);
}

.card-row {
    width: 100%;
}

.card-row:nth-child(2) {
    margin: 15px 0;
    color: var(--accents-6);
    font-size: 0.875rem;
    font-weight: 500;
    line-height: 1.25rem;
    letter-spacing: initial;
    -webkit-line-clamp: 2;
}

.card-row:nth-child(3) {
    color: #666;
    font-size: 0.875rem;
    line-height: 1.25rem;
    letter-spacing: initial;
    font-weight: 400;
}

.card-row .title {
    display: flex;
    align-items: center;
}

.card-row .title img {
    height: 32px;
    width: 32px;
    margin-right: 10px;
}

.card-row .title > div p:nth-child(2) {
    color: #535353;
    font-size: 0.875rem;
    line-height: 1.25rem;
    letter-spacing: initial;
    font-weight: 400;
}

.menu-wrapper {
    position: absolute;
    inset: 0px auto auto 0px;
    opacity: 0;
    z-index: 110;
    transition: opacity 0.15s;
    pointer-events: none;
}

.menu-wrapper.active {
    display: block;
    opacity: 1;
    user-select: none;
    pointer-events: auto;
}

.menu-wrapper ul {
    min-width: 128px;
    width: auto;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    border-radius: 5px;
    font-size: 0.875rem;
    outline: none;
    background: #fff;
    border: 1px solid #eaeaea;
    overflow: auto;
    -webkit-overflow-scrolling: touch;
    padding: 8px;
}

.menu-wrapper ul li {
    color: #000;
    outline: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    padding: 0 8px;
    height: 36px;
    border-radius: 5px;
}

.menu-wrapper ul li:hover {
    background: #eaeaea;
}

.project-row {
    position: relative;
    box-sizing: border-box;
    padding: 16px;
    margin-bottom: 20px;
    background: #fff;
    border: 1px solid #eaeaea;
    height: 80px;
    max-height: auto;
    transition: max-height 0.5s ease-in;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
    border-radius: 5px;
    cursor: pointer;
}

.row-container {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    min-width: 1px;
    max-width: 100%;
    justify-content: flex-start;
    align-items: stretch;
}

.row-container .l-part {
    position: relative;
    display: flex;
    flex-direction: row;
    flex: 0 0 70%;
    flex-wrap: wrap;
    min-width: 1px;
    max-width: 100%;
    justify-content: flex-start;
    align-items: center;
}

.row-container .l-part .avatar {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
}

.row-container .l-part .content {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 1px;
    max-width: 100%;
    flex: 1;
    justify-content: center;
    align-items: stretch;
}
.row-container .r-part p,
.row-container .l-part .content p {
    font-weight: bold;
    font-size: 0.875rem;
    line-height: 1.6;
    color: #000;
}

.row-container .r-part p:nth-child(2),
.row-container .l-part .content p:nth-child(2) {
    font-weight: 400;
    color: rgb(102, 102, 102);
}

.underline:hover {
    text-decoration: underline;
}

.share-svg {
    vertical-align: middle;
    visibility: hidden;
    margin-left: 3px;
    text-decoration: none;
}

.underline:hover .share-svg {
    visibility: visible;
}

.row-container .r-part {
    position: relative;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    min-width: 1;
    max-width: 100%;
    flex: 1;
    justify-content: flex-start;
    align-items: center;
}

.store .alter {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100vh;
}

.alter .header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    min-height: 137px;
    max-height: 137px;
    background-color: #fff;
    border-bottom: 1px solid #eaeaea;
    padding: 0 24px;
    transition: height 0.5s ease-in-out;
}
.alter .header .header-title {
    display: flex;
    align-items: stretch;
    justify-content: flex-start;
    flex: initial;
}

.alter .header .header-title .header-title-left {
    flex: 1;
    color: #000;
    font-size: 2rem;
    line-height: 2.5rem;
    letter-spacing: -0.049375rem;
    font-weight: 500;
}

.alter .header .header-title .header-title-right {
    display: flex;
    justify-content: center;
    align-items: center;
}

.alter .header .header-title .header-title-right button {
    margin-left: 15px;
}

.header-title-right {
    opacity: 1;
}

.alter .dashboard {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100%;

    overflow-y: auto;
}

.alter .dashboard-card-wrapper {
    padding: 48px 0;
    display: flex;
    flex-direction: column;
    position: relative;
    height: auto;
}

.dashboard-card-header {
    display: flex;
    flex-direction: column;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.6;
    color: #444;
}

.dashboard-card-header .dashboard-card-header-title {
    font-size: 1.5rem;
    letter-spacing: -0.029375rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.dashboard-card {
    margin-top: 2.5rem;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.12);
    background: #fff;
    border-radius: 5px;
    border: 1px solid #eaeaea;
    position: relative;
    overflow: hidden;

    padding: 24px;
}

.fieldset-content {
    position: relative;
    display: flex;
    justify-content: flex-start;
    align-items: stretch;
    width: 100%;
    position: relative;
    background-color: #fff;
}

.fieldset-content .screenshot {
    flex: 0 0 auto;
    cursor: pointer;
}

.fieldset-content .screenshot img {
    width: 100%;
    height: 100%;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    object-fit: cover;
}

.fieldset-content .dashboard-meta {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: stretch;
    margin-left: 2rem;
}

.meta-row h3 {
    margin-bottom: 3px;
    line-height: 18px;
    font-weight: 500;
    font-size: 1rem;
    text-transform: uppercase;
    white-space: nowrap;
    color: #666;
}

.meta-row p {
    text-decoration: none;
    color: #000;
    font-weight: 500;
    font-size: 0.95rem;
    overflow: hidden;
    white-space: nowrap;
    display: inline-block;
    text-overflow: ellipsis;
}

@media (min-width: 1875px) {
    /* Styles for screens wider than 1875px */
    .dashboard-card-wrapper {
        width: 1500px;
    }
    .screenshot {
        width: 570px;
        height: 356px;
    }
}

@media (max-width: 1874px) {
    /* Styles for screens narrower than 1875px */
    .dashboard-card-wrapper {
        width: 70vw;
    }
    .screenshot {
        width: 26.6vw;
        height: 16.625vw;
    }
}

.configure-content {
    margin-top: 2rem;
}

.configure-content hr {
    margin: 16px 0;
    border-bottom: 1px solid #eaeaea;
}

.configure-title h2 {
    font-size: 1.5rem;
    letter-spacing: -0.029375rem;
    font-weight: 600;
}

.configure-setting {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
}

.setting-row {
    margin-bottom: 0.8rem;
}

.setting-row-title {
    margin-bottom: 0.5rem;
}

.setting-row-title h4 {
    color: #666;
    font-weight: 500;
    font-size: 0.8rem;
}

.setting-row-content input {
    display: inline-flex;
    font-size: 14px;
    width: 100%;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    padding: 0 12px;
    background: var(--themed-bg, var(--geist-background));
    color: #000;
    height: 40px;
    transition: border-color 0.15s ease;
    -webkit-tap-highlight-color: transparent;
}

.setting-block details[open],
.setting-row-content select:focus,
.setting-row-content input:focus,
.setting-row-content textarea:focus {
    border-color: #000;
}

.setting-row-content select {
    font-size: 0.875rem;
    height: 40px;
    line-height: 1.25rem;
    text-rendering: auto;
    width: 100%;
    border-radius: 5px;
    border: 1px solid #eaeaea;
    background: #fff;
    color: #000;
    padding: 0 12px;
    cursor: pointer;
}

.setting-row-content textarea {
    padding: 5px 12px;
    resize: none;
    width: 100%;
    height: 75px;
    font-size: 0.875rem;
    line-height: 1.25rem;
    text-rendering: auto;
    border-radius: 5px;
    border: 1px solid #eaeaea;
    background: #fff;
}

.setting-block {
    overflow: hidden;
    margin-bottom: 1rem;
}

.setting-block details {
    background-color: #fff;
    color: #444;
    padding: 12px;
    border: 1px solid #eaeaea;
    border-radius: 5px;
}

details[open] summary:before {
    transform: rotate(90deg);
}

.setting-block details summary {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
    width: 100%;
    margin-bottom: 12px;
    font-size: 14px;
    list-style: none;
    color: #444;
    margin: -12px;
    padding: 12px;
}
/* 使用自定义图标 */

summary::-webkit-details-marker {
    display: none;
}
summary:before {
    content: '\003E'; /* the new icon */
    color: #696f7c;
    margin-right: 5px;
    transition: transform 0.3s;
}

.setting-block details > div {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
    margin-top: 1rem;
}

.account-block {
    position: relative;
    width: 100%;
    margin-bottom: 1rem;
}

.account-block-title {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
}

.account-block-title p {
    font-size: 12px;
    font-weight: 500;
    color: #666;
    margin-right: 5px;
}

.account-block-content {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.account-block-content input {
    display: inline-flex;
    font-size: 14px;
    width: 80%;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    padding: 0 12px;
    background: var(--themed-bg, var(--geist-background));
    color: #000;
    height: 40px;
    transition: border-color 0.15s ease;
    -webkit-tap-highlight-color: transparent;
}

input.disabled {
    cursor: not-allowed;
    color: #666;
    background-color: #fafafa;
}

.deploy-step {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
    height: 64px;
    width: 100%;
    color: #999;
    font-size: 14px;
    font-weight: 700;
    border: 1px solid #eaeaea;
    border-bottom: 0;
}

.deploy-step:first-of-type {
    border-radius: 5px 5px 0 0;
}

.deploy-step:last-of-type {
    border-radius: 0 0 5px 5px;
    border-bottom: 1px solid #eaeaea;
}

.spinner {
    /* Size */
    height: 1.5rem;
    width: 1.5rem;

    /* Create a curve at the top */
    border: 4px solid #d1d5db;
    border-radius: 50%;
}

.spinner.run {
    border-top-color: #3b82f6;
    animation: spinner 800ms linear infinite;
}

.spinner.over {
    animation: none;
    border-color: #3b82f6;
}

@keyframes spinner {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
</style>
