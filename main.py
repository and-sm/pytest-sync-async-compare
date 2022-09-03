from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>

        <body>
<button id="id_1">1</button>
<button id="id_2">2</button>
<button id="id_3">3</button>
<button id="id_4">4</button>
<button id="id_5">5</button>
<button id="id_6">6</button>
<button id="id_7">7</button>
<button id="id_8">8</button>
<button id="id_9">9</button>
<button id="id_10">10</button>
<button id="id_11">11</button>
<button id="id_12">12</button>
<button id="id_13">13</button>
<button id="id_14">14</button>
<button id="id_15">15</button>
<button id="id_16">16</button>
<button id="id_17">17</button>
<button id="id_18">18</button>
<button id="id_19">19</button>
<button id="id_20">20</button>
<button id="id_21">21</button>
<button id="id_22">22</button>
<button id="id_23">23</button>
<button id="id_24">24</button>
<button id="id_25">25</button>
<button id="id_26">26</button>
<button id="id_27">27</button>
<button id="id_28">28</button>
<button id="id_29">29</button>
<button id="id_30">30</button>
<button id="id_31">31</button>
<button id="id_32">32</button>
<button id="id_33">33</button>
<button id="id_34">34</button>
<button id="id_35">35</button>
<button id="id_36">36</button>
<button id="id_37">37</button>
<button id="id_38">38</button>
<button id="id_39">39</button>
<button id="id_40">40</button>
<button id="id_41">41</button>
<button id="id_42">42</button>
<button id="id_43">43</button>
<button id="id_44">44</button>
<button id="id_45">45</button>
<button id="id_46">46</button>
<button id="id_47">47</button>
<button id="id_48">48</button>
<button id="id_49">49</button>
<button id="id_50">50</button>
<button id="id_51">51</button>
<button id="id_52">52</button>
<button id="id_53">53</button>
<button id="id_54">54</button>
<button id="id_55">55</button>
<button id="id_56">56</button>
<button id="id_57">57</button>
<button id="id_58">58</button>
<button id="id_59">59</button>
<button id="id_60">60</button>
<button id="id_61">61</button>
<button id="id_62">62</button>
<button id="id_63">63</button>
<button id="id_64">64</button>
<button id="id_65">65</button>
<button id="id_66">66</button>
<button id="id_67">67</button>
<button id="id_68">68</button>
<button id="id_69">69</button>
<button id="id_70">70</button>
<button id="id_71">71</button>
<button id="id_72">72</button>
<button id="id_73">73</button>
<button id="id_74">74</button>
<button id="id_75">75</button>
<button id="id_76">76</button>
<button id="id_77">77</button>
<button id="id_78">78</button>
<button id="id_79">79</button>
<button id="id_80">80</button>
<button id="id_81">81</button>
<button id="id_82">82</button>
<button id="id_83">83</button>
<button id="id_84">84</button>
<button id="id_85">85</button>
<button id="id_86">86</button>
<button id="id_87">87</button>
<button id="id_88">88</button>
<button id="id_89">89</button>
<button id="id_90">90</button>
<button id="id_91">91</button>
<button id="id_92">92</button>
<button id="id_93">93</button>
<button id="id_94">94</button>
<button id="id_95">95</button>
<button id="id_96">96</button>
<button id="id_97">97</button>
<button id="id_98">98</button>
<button id="id_99">99</button>
<button id="id_100">100</button>
<button id="id_101">101</button>
<button id="id_102">102</button>
<button id="id_103">103</button>
<button id="id_104">104</button>
<button id="id_105">105</button>
<button id="id_106">106</button>
<button id="id_107">107</button>
<button id="id_108">108</button>
<button id="id_109">109</button>
<button id="id_110">110</button>
<button id="id_111">111</button>
<button id="id_112">112</button>
<button id="id_113">113</button>
<button id="id_114">114</button>
<button id="id_115">115</button>
<button id="id_116">116</button>
<button id="id_117">117</button>
<button id="id_118">118</button>
<button id="id_119">119</button>
<button id="id_120">120</button>
<button id="id_121">121</button>
<button id="id_122">122</button>
<button id="id_123">123</button>
<button id="id_124">124</button>
<button id="id_125">125</button>
<button id="id_126">126</button>
<button id="id_127">127</button>
<button id="id_128">128</button>
<button id="id_129">129</button>
<button id="id_130">130</button>
<button id="id_131">131</button>
<button id="id_132">132</button>
<button id="id_133">133</button>
<button id="id_134">134</button>
<button id="id_135">135</button>
<button id="id_136">136</button>
<button id="id_137">137</button>
<button id="id_138">138</button>
<button id="id_139">139</button>
<button id="id_140">140</button>
<button id="id_141">141</button>
<button id="id_142">142</button>
<button id="id_143">143</button>
<button id="id_144">144</button>
<button id="id_145">145</button>
<button id="id_146">146</button>
<button id="id_147">147</button>
<button id="id_148">148</button>
<button id="id_149">149</button>
<button id="id_150">150</button>
<button id="id_151">151</button>
<button id="id_152">152</button>
<button id="id_153">153</button>
<button id="id_154">154</button>
<button id="id_155">155</button>
<button id="id_156">156</button>
<button id="id_157">157</button>
<button id="id_158">158</button>
<button id="id_159">159</button>
<button id="id_160">160</button>
<button id="id_161">161</button>
<button id="id_162">162</button>
<button id="id_163">163</button>
<button id="id_164">164</button>
<button id="id_165">165</button>
<button id="id_166">166</button>
<button id="id_167">167</button>
<button id="id_168">168</button>
<button id="id_169">169</button>
<button id="id_170">170</button>
<button id="id_171">171</button>
<button id="id_172">172</button>
<button id="id_173">173</button>
<button id="id_174">174</button>
<button id="id_175">175</button>
<button id="id_176">176</button>
<button id="id_177">177</button>
<button id="id_178">178</button>
<button id="id_179">179</button>
<button id="id_180">180</button>
<button id="id_181">181</button>
<button id="id_182">182</button>
<button id="id_183">183</button>
<button id="id_184">184</button>
<button id="id_185">185</button>
<button id="id_186">186</button>
<button id="id_187">187</button>
<button id="id_188">188</button>
<button id="id_189">189</button>
<button id="id_190">190</button>
<button id="id_191">191</button>
<button id="id_192">192</button>
<button id="id_193">193</button>
<button id="id_194">194</button>
<button id="id_195">195</button>
<button id="id_196">196</button>
<button id="id_197">197</button>
<button id="id_198">198</button>
<button id="id_199">199</button>
<button id="id_200">200</button>
<button id="id_201">201</button>
<button id="id_202">202</button>
<button id="id_203">203</button>
<button id="id_204">204</button>
<button id="id_205">205</button>
<button id="id_206">206</button>
<button id="id_207">207</button>
<button id="id_208">208</button>
<button id="id_209">209</button>
<button id="id_210">210</button>
<button id="id_211">211</button>
<button id="id_212">212</button>
<button id="id_213">213</button>
<button id="id_214">214</button>
<button id="id_215">215</button>
<button id="id_216">216</button>
<button id="id_217">217</button>
<button id="id_218">218</button>
<button id="id_219">219</button>
<button id="id_220">220</button>
<button id="id_221">221</button>
<button id="id_222">222</button>
<button id="id_223">223</button>
<button id="id_224">224</button>
<button id="id_225">225</button>
<button id="id_226">226</button>
<button id="id_227">227</button>
<button id="id_228">228</button>
<button id="id_229">229</button>
<button id="id_230">230</button>
<button id="id_231">231</button>
<button id="id_232">232</button>
<button id="id_233">233</button>
<button id="id_234">234</button>
<button id="id_235">235</button>
<button id="id_236">236</button>
<button id="id_237">237</button>
<button id="id_238">238</button>
<button id="id_239">239</button>
<button id="id_240">240</button>
<button id="id_241">241</button>
<button id="id_242">242</button>
<button id="id_243">243</button>
<button id="id_244">244</button>
<button id="id_245">245</button>
<button id="id_246">246</button>
<button id="id_247">247</button>
<button id="id_248">248</button>
<button id="id_249">249</button>
<button id="id_250">250</button>
<button id="id_251">251</button>
<button id="id_252">252</button>
<button id="id_253">253</button>
<button id="id_254">254</button>
<button id="id_255">255</button>
<button id="id_256">256</button>
<button id="id_257">257</button>
<button id="id_258">258</button>
<button id="id_259">259</button>
<button id="id_260">260</button>
<button id="id_261">261</button>
<button id="id_262">262</button>
<button id="id_263">263</button>
<button id="id_264">264</button>
<button id="id_265">265</button>
<button id="id_266">266</button>
<button id="id_267">267</button>
<button id="id_268">268</button>
<button id="id_269">269</button>
<button id="id_270">270</button>
<button id="id_271">271</button>
<button id="id_272">272</button>
<button id="id_273">273</button>
<button id="id_274">274</button>
<button id="id_275">275</button>
<button id="id_276">276</button>
<button id="id_277">277</button>
<button id="id_278">278</button>
<button id="id_279">279</button>
<button id="id_280">280</button>
<button id="id_281">281</button>
<button id="id_282">282</button>
<button id="id_283">283</button>
<button id="id_284">284</button>
<button id="id_285">285</button>
<button id="id_286">286</button>
<button id="id_287">287</button>
<button id="id_288">288</button>
<button id="id_289">289</button>
<button id="id_290">290</button>
<button id="id_291">291</button>
<button id="id_292">292</button>
<button id="id_293">293</button>
<button id="id_294">294</button>
<button id="id_295">295</button>
<button id="id_296">296</button>
<button id="id_297">297</button>
<button id="id_298">298</button>
<button id="id_299">299</button>
<button id="id_300">300</button>
<button id="id_301">301</button>
<button id="id_302">302</button>
<button id="id_303">303</button>
<button id="id_304">304</button>
<button id="id_305">305</button>
<button id="id_306">306</button>
<button id="id_307">307</button>
<button id="id_308">308</button>
<button id="id_309">309</button>
<button id="id_310">310</button>
<button id="id_311">311</button>
<button id="id_312">312</button>
<button id="id_313">313</button>
<button id="id_314">314</button>
<button id="id_315">315</button>
<button id="id_316">316</button>
<button id="id_317">317</button>
<button id="id_318">318</button>
<button id="id_319">319</button>
<button id="id_320">320</button>
<button id="id_321">321</button>
<button id="id_322">322</button>
<button id="id_323">323</button>
<button id="id_324">324</button>
<button id="id_325">325</button>
<button id="id_326">326</button>
<button id="id_327">327</button>
<button id="id_328">328</button>
<button id="id_329">329</button>
<button id="id_330">330</button>
<button id="id_331">331</button>
<button id="id_332">332</button>
<button id="id_333">333</button>
<button id="id_334">334</button>
<button id="id_335">335</button>
<button id="id_336">336</button>
<button id="id_337">337</button>
<button id="id_338">338</button>
<button id="id_339">339</button>
<button id="id_340">340</button>
<button id="id_341">341</button>
<button id="id_342">342</button>
<button id="id_343">343</button>
<button id="id_344">344</button>
<button id="id_345">345</button>
<button id="id_346">346</button>
<button id="id_347">347</button>
<button id="id_348">348</button>
<button id="id_349">349</button>
<button id="id_350">350</button>
<button id="id_351">351</button>
<button id="id_352">352</button>
<button id="id_353">353</button>
<button id="id_354">354</button>
<button id="id_355">355</button>
<button id="id_356">356</button>
<button id="id_357">357</button>
<button id="id_358">358</button>
<button id="id_359">359</button>
<button id="id_360">360</button>
<button id="id_361">361</button>
<button id="id_362">362</button>
<button id="id_363">363</button>
<button id="id_364">364</button>
<button id="id_365">365</button>
<button id="id_366">366</button>
<button id="id_367">367</button>
<button id="id_368">368</button>
<button id="id_369">369</button>
<button id="id_370">370</button>
<button id="id_371">371</button>
<button id="id_372">372</button>
<button id="id_373">373</button>
<button id="id_374">374</button>
<button id="id_375">375</button>
<button id="id_376">376</button>
<button id="id_377">377</button>
<button id="id_378">378</button>
<button id="id_379">379</button>
<button id="id_380">380</button>
<button id="id_381">381</button>
<button id="id_382">382</button>
<button id="id_383">383</button>
<button id="id_384">384</button>
<button id="id_385">385</button>
<button id="id_386">386</button>
<button id="id_387">387</button>
<button id="id_388">388</button>
<button id="id_389">389</button>
<button id="id_390">390</button>
<button id="id_391">391</button>
<button id="id_392">392</button>
<button id="id_393">393</button>
<button id="id_394">394</button>
<button id="id_395">395</button>
<button id="id_396">396</button>
<button id="id_397">397</button>
<button id="id_398">398</button>
<button id="id_399">399</button>
<button id="id_400">400</button>
<button id="id_401">401</button>
<button id="id_402">402</button>
<button id="id_403">403</button>
<button id="id_404">404</button>
<button id="id_405">405</button>
<button id="id_406">406</button>
<button id="id_407">407</button>
<button id="id_408">408</button>
<button id="id_409">409</button>
<button id="id_410">410</button>
<button id="id_411">411</button>
<button id="id_412">412</button>
<button id="id_413">413</button>
<button id="id_414">414</button>
<button id="id_415">415</button>
<button id="id_416">416</button>
<button id="id_417">417</button>
<button id="id_418">418</button>
<button id="id_419">419</button>
<button id="id_420">420</button>
<button id="id_421">421</button>
<button id="id_422">422</button>
<button id="id_423">423</button>
<button id="id_424">424</button>
<button id="id_425">425</button>
<button id="id_426">426</button>
<button id="id_427">427</button>
<button id="id_428">428</button>
<button id="id_429">429</button>
<button id="id_430">430</button>
<button id="id_431">431</button>
<button id="id_432">432</button>
<button id="id_433">433</button>
<button id="id_434">434</button>
<button id="id_435">435</button>
<button id="id_436">436</button>
<button id="id_437">437</button>
<button id="id_438">438</button>
<button id="id_439">439</button>
<button id="id_440">440</button>
<button id="id_441">441</button>
<button id="id_442">442</button>
<button id="id_443">443</button>
<button id="id_444">444</button>
<button id="id_445">445</button>
<button id="id_446">446</button>
<button id="id_447">447</button>
<button id="id_448">448</button>
<button id="id_449">449</button>
<button id="id_450">450</button>
<button id="id_451">451</button>
<button id="id_452">452</button>
<button id="id_453">453</button>
<button id="id_454">454</button>
<button id="id_455">455</button>
<button id="id_456">456</button>
<button id="id_457">457</button>
<button id="id_458">458</button>
<button id="id_459">459</button>
<button id="id_460">460</button>
<button id="id_461">461</button>
<button id="id_462">462</button>
<button id="id_463">463</button>
<button id="id_464">464</button>
<button id="id_465">465</button>
<button id="id_466">466</button>
<button id="id_467">467</button>
<button id="id_468">468</button>
<button id="id_469">469</button>
<button id="id_470">470</button>
<button id="id_471">471</button>
<button id="id_472">472</button>
<button id="id_473">473</button>
<button id="id_474">474</button>
<button id="id_475">475</button>
<button id="id_476">476</button>
<button id="id_477">477</button>
<button id="id_478">478</button>
<button id="id_479">479</button>
<button id="id_480">480</button>
<button id="id_481">481</button>
<button id="id_482">482</button>
<button id="id_483">483</button>
<button id="id_484">484</button>
<button id="id_485">485</button>
<button id="id_486">486</button>
<button id="id_487">487</button>
<button id="id_488">488</button>
<button id="id_489">489</button>
<button id="id_490">490</button>
<button id="id_491">491</button>
<button id="id_492">492</button>
<button id="id_493">493</button>
<button id="id_494">494</button>
<button id="id_495">495</button>
<button id="id_496">496</button>
<button id="id_497">497</button>
<button id="id_498">498</button>
<button id="id_499">499</button>
<button id="id_500">500</button>
<button id="id_501">501</button>
<button id="id_502">502</button>
<button id="id_503">503</button>
<button id="id_504">504</button>
<button id="id_505">505</button>
<button id="id_506">506</button>
<button id="id_507">507</button>
<button id="id_508">508</button>
<button id="id_509">509</button>
<button id="id_510">510</button>
<button id="id_511">511</button>
<button id="id_512">512</button>
<button id="id_513">513</button>
<button id="id_514">514</button>
<button id="id_515">515</button>
<button id="id_516">516</button>
<button id="id_517">517</button>
<button id="id_518">518</button>
<button id="id_519">519</button>
<button id="id_520">520</button>
<button id="id_521">521</button>
<button id="id_522">522</button>
<button id="id_523">523</button>
<button id="id_524">524</button>
<button id="id_525">525</button>
<button id="id_526">526</button>
<button id="id_527">527</button>
<button id="id_528">528</button>
<button id="id_529">529</button>
<button id="id_530">530</button>
<button id="id_531">531</button>
<button id="id_532">532</button>
<button id="id_533">533</button>
<button id="id_534">534</button>
<button id="id_535">535</button>
<button id="id_536">536</button>
<button id="id_537">537</button>
<button id="id_538">538</button>
<button id="id_539">539</button>
<button id="id_540">540</button>
<button id="id_541">541</button>
<button id="id_542">542</button>
<button id="id_543">543</button>
<button id="id_544">544</button>
<button id="id_545">545</button>
<button id="id_546">546</button>
<button id="id_547">547</button>
<button id="id_548">548</button>
<button id="id_549">549</button>
<button id="id_550">550</button>
<button id="id_551">551</button>
<button id="id_552">552</button>
<button id="id_553">553</button>
<button id="id_554">554</button>
<button id="id_555">555</button>
<button id="id_556">556</button>
<button id="id_557">557</button>
<button id="id_558">558</button>
<button id="id_559">559</button>
<button id="id_560">560</button>
<button id="id_561">561</button>
<button id="id_562">562</button>
<button id="id_563">563</button>
<button id="id_564">564</button>
<button id="id_565">565</button>
<button id="id_566">566</button>
<button id="id_567">567</button>
<button id="id_568">568</button>
<button id="id_569">569</button>
<button id="id_570">570</button>
<button id="id_571">571</button>
<button id="id_572">572</button>
<button id="id_573">573</button>
<button id="id_574">574</button>
<button id="id_575">575</button>
<button id="id_576">576</button>
<button id="id_577">577</button>
<button id="id_578">578</button>
<button id="id_579">579</button>
<button id="id_580">580</button>
<button id="id_581">581</button>
<button id="id_582">582</button>
<button id="id_583">583</button>
<button id="id_584">584</button>
<button id="id_585">585</button>
<button id="id_586">586</button>
<button id="id_587">587</button>
<button id="id_588">588</button>
<button id="id_589">589</button>
<button id="id_590">590</button>
<button id="id_591">591</button>
<button id="id_592">592</button>
<button id="id_593">593</button>
<button id="id_594">594</button>
<button id="id_595">595</button>
<button id="id_596">596</button>
<button id="id_597">597</button>
<button id="id_598">598</button>
<button id="id_599">599</button>
<button id="id_600">600</button>
<button id="id_601">601</button>
<button id="id_602">602</button>
<button id="id_603">603</button>
<button id="id_604">604</button>
<button id="id_605">605</button>
<button id="id_606">606</button>
<button id="id_607">607</button>
<button id="id_608">608</button>
<button id="id_609">609</button>
<button id="id_610">610</button>
<button id="id_611">611</button>
<button id="id_612">612</button>
<button id="id_613">613</button>
<button id="id_614">614</button>
<button id="id_615">615</button>
<button id="id_616">616</button>
<button id="id_617">617</button>
<button id="id_618">618</button>
<button id="id_619">619</button>
<button id="id_620">620</button>
<button id="id_621">621</button>
<button id="id_622">622</button>
<button id="id_623">623</button>
<button id="id_624">624</button>
<button id="id_625">625</button>
<button id="id_626">626</button>
<button id="id_627">627</button>
<button id="id_628">628</button>
<button id="id_629">629</button>
<button id="id_630">630</button>
<button id="id_631">631</button>
<button id="id_632">632</button>
<button id="id_633">633</button>
<button id="id_634">634</button>
<button id="id_635">635</button>
<button id="id_636">636</button>
<button id="id_637">637</button>
<button id="id_638">638</button>
<button id="id_639">639</button>
<button id="id_640">640</button>
<button id="id_641">641</button>
<button id="id_642">642</button>
<button id="id_643">643</button>
<button id="id_644">644</button>
<button id="id_645">645</button>
<button id="id_646">646</button>
<button id="id_647">647</button>
<button id="id_648">648</button>
<button id="id_649">649</button>
<button id="id_650">650</button>
<button id="id_651">651</button>
<button id="id_652">652</button>
<button id="id_653">653</button>
<button id="id_654">654</button>
<button id="id_655">655</button>
<button id="id_656">656</button>
<button id="id_657">657</button>
<button id="id_658">658</button>
<button id="id_659">659</button>
<button id="id_660">660</button>
<button id="id_661">661</button>
<button id="id_662">662</button>
<button id="id_663">663</button>
<button id="id_664">664</button>
<button id="id_665">665</button>
<button id="id_666">666</button>
<button id="id_667">667</button>
<button id="id_668">668</button>
<button id="id_669">669</button>
<button id="id_670">670</button>
<button id="id_671">671</button>
<button id="id_672">672</button>
<button id="id_673">673</button>
<button id="id_674">674</button>
<button id="id_675">675</button>
<button id="id_676">676</button>
<button id="id_677">677</button>
<button id="id_678">678</button>
<button id="id_679">679</button>
<button id="id_680">680</button>
<button id="id_681">681</button>
<button id="id_682">682</button>
<button id="id_683">683</button>
<button id="id_684">684</button>
<button id="id_685">685</button>
<button id="id_686">686</button>
<button id="id_687">687</button>
<button id="id_688">688</button>
<button id="id_689">689</button>
<button id="id_690">690</button>
<button id="id_691">691</button>
<button id="id_692">692</button>
<button id="id_693">693</button>
<button id="id_694">694</button>
<button id="id_695">695</button>
<button id="id_696">696</button>
<button id="id_697">697</button>
<button id="id_698">698</button>
<button id="id_699">699</button>
<button id="id_700">700</button>
<button id="id_701">701</button>
<button id="id_702">702</button>
<button id="id_703">703</button>
<button id="id_704">704</button>
<button id="id_705">705</button>
<button id="id_706">706</button>
<button id="id_707">707</button>
<button id="id_708">708</button>
<button id="id_709">709</button>
<button id="id_710">710</button>
<button id="id_711">711</button>
<button id="id_712">712</button>
<button id="id_713">713</button>
<button id="id_714">714</button>
<button id="id_715">715</button>
<button id="id_716">716</button>
<button id="id_717">717</button>
<button id="id_718">718</button>
<button id="id_719">719</button>
<button id="id_720">720</button>
<button id="id_721">721</button>
<button id="id_722">722</button>
<button id="id_723">723</button>
<button id="id_724">724</button>
<button id="id_725">725</button>
<button id="id_726">726</button>
<button id="id_727">727</button>
<button id="id_728">728</button>
<button id="id_729">729</button>
<button id="id_730">730</button>
<button id="id_731">731</button>
<button id="id_732">732</button>
<button id="id_733">733</button>
<button id="id_734">734</button>
<button id="id_735">735</button>
<button id="id_736">736</button>
<button id="id_737">737</button>
<button id="id_738">738</button>
<button id="id_739">739</button>
<button id="id_740">740</button>
<button id="id_741">741</button>
<button id="id_742">742</button>
<button id="id_743">743</button>
<button id="id_744">744</button>
<button id="id_745">745</button>
<button id="id_746">746</button>
<button id="id_747">747</button>
<button id="id_748">748</button>
<button id="id_749">749</button>
<button id="id_750">750</button>
<button id="id_751">751</button>
<button id="id_752">752</button>
<button id="id_753">753</button>
<button id="id_754">754</button>
<button id="id_755">755</button>
<button id="id_756">756</button>
<button id="id_757">757</button>
<button id="id_758">758</button>
<button id="id_759">759</button>
<button id="id_760">760</button>
<button id="id_761">761</button>
<button id="id_762">762</button>
<button id="id_763">763</button>
<button id="id_764">764</button>
<button id="id_765">765</button>
<button id="id_766">766</button>
<button id="id_767">767</button>
<button id="id_768">768</button>
<button id="id_769">769</button>
<button id="id_770">770</button>
<button id="id_771">771</button>
<button id="id_772">772</button>
<button id="id_773">773</button>
<button id="id_774">774</button>
<button id="id_775">775</button>
<button id="id_776">776</button>
<button id="id_777">777</button>
<button id="id_778">778</button>
<button id="id_779">779</button>
<button id="id_780">780</button>
<button id="id_781">781</button>
<button id="id_782">782</button>
<button id="id_783">783</button>
<button id="id_784">784</button>
<button id="id_785">785</button>
<button id="id_786">786</button>
<button id="id_787">787</button>
<button id="id_788">788</button>
<button id="id_789">789</button>
<button id="id_790">790</button>
<button id="id_791">791</button>
<button id="id_792">792</button>
<button id="id_793">793</button>
<button id="id_794">794</button>
<button id="id_795">795</button>
<button id="id_796">796</button>
<button id="id_797">797</button>
<button id="id_798">798</button>
<button id="id_799">799</button>
<button id="id_800">800</button>
<button id="id_801">801</button>
<button id="id_802">802</button>
<button id="id_803">803</button>
<button id="id_804">804</button>
<button id="id_805">805</button>
<button id="id_806">806</button>
<button id="id_807">807</button>
<button id="id_808">808</button>
<button id="id_809">809</button>
<button id="id_810">810</button>
<button id="id_811">811</button>
<button id="id_812">812</button>
<button id="id_813">813</button>
<button id="id_814">814</button>
<button id="id_815">815</button>
<button id="id_816">816</button>
<button id="id_817">817</button>
<button id="id_818">818</button>
<button id="id_819">819</button>
<button id="id_820">820</button>
<button id="id_821">821</button>
<button id="id_822">822</button>
<button id="id_823">823</button>
<button id="id_824">824</button>
<button id="id_825">825</button>
<button id="id_826">826</button>
<button id="id_827">827</button>
<button id="id_828">828</button>
<button id="id_829">829</button>
<button id="id_830">830</button>
<button id="id_831">831</button>
<button id="id_832">832</button>
<button id="id_833">833</button>
<button id="id_834">834</button>
<button id="id_835">835</button>
<button id="id_836">836</button>
<button id="id_837">837</button>
<button id="id_838">838</button>
<button id="id_839">839</button>
<button id="id_840">840</button>
<button id="id_841">841</button>
<button id="id_842">842</button>
<button id="id_843">843</button>
<button id="id_844">844</button>
<button id="id_845">845</button>
<button id="id_846">846</button>
<button id="id_847">847</button>
<button id="id_848">848</button>
<button id="id_849">849</button>
<button id="id_850">850</button>
<button id="id_851">851</button>
<button id="id_852">852</button>
<button id="id_853">853</button>
<button id="id_854">854</button>
<button id="id_855">855</button>
<button id="id_856">856</button>
<button id="id_857">857</button>
<button id="id_858">858</button>
<button id="id_859">859</button>
<button id="id_860">860</button>
<button id="id_861">861</button>
<button id="id_862">862</button>
<button id="id_863">863</button>
<button id="id_864">864</button>
<button id="id_865">865</button>
<button id="id_866">866</button>
<button id="id_867">867</button>
<button id="id_868">868</button>
<button id="id_869">869</button>
<button id="id_870">870</button>
<button id="id_871">871</button>
<button id="id_872">872</button>
<button id="id_873">873</button>
<button id="id_874">874</button>
<button id="id_875">875</button>
<button id="id_876">876</button>
<button id="id_877">877</button>
<button id="id_878">878</button>
<button id="id_879">879</button>
<button id="id_880">880</button>
<button id="id_881">881</button>
<button id="id_882">882</button>
<button id="id_883">883</button>
<button id="id_884">884</button>
<button id="id_885">885</button>
<button id="id_886">886</button>
<button id="id_887">887</button>
<button id="id_888">888</button>
<button id="id_889">889</button>
<button id="id_890">890</button>
<button id="id_891">891</button>
<button id="id_892">892</button>
<button id="id_893">893</button>
<button id="id_894">894</button>
<button id="id_895">895</button>
<button id="id_896">896</button>
<button id="id_897">897</button>
<button id="id_898">898</button>
<button id="id_899">899</button>
<button id="id_900">900</button>
<button id="id_901">901</button>
<button id="id_902">902</button>
<button id="id_903">903</button>
<button id="id_904">904</button>
<button id="id_905">905</button>
<button id="id_906">906</button>
<button id="id_907">907</button>
<button id="id_908">908</button>
<button id="id_909">909</button>
<button id="id_910">910</button>
<button id="id_911">911</button>
<button id="id_912">912</button>
<button id="id_913">913</button>
<button id="id_914">914</button>
<button id="id_915">915</button>
<button id="id_916">916</button>
<button id="id_917">917</button>
<button id="id_918">918</button>
<button id="id_919">919</button>
<button id="id_920">920</button>
<button id="id_921">921</button>
<button id="id_922">922</button>
<button id="id_923">923</button>
<button id="id_924">924</button>
<button id="id_925">925</button>
<button id="id_926">926</button>
<button id="id_927">927</button>
<button id="id_928">928</button>
<button id="id_929">929</button>
<button id="id_930">930</button>
<button id="id_931">931</button>
<button id="id_932">932</button>
<button id="id_933">933</button>
<button id="id_934">934</button>
<button id="id_935">935</button>
<button id="id_936">936</button>
<button id="id_937">937</button>
<button id="id_938">938</button>
<button id="id_939">939</button>
<button id="id_940">940</button>
<button id="id_941">941</button>
<button id="id_942">942</button>
<button id="id_943">943</button>
<button id="id_944">944</button>
<button id="id_945">945</button>
<button id="id_946">946</button>
<button id="id_947">947</button>
<button id="id_948">948</button>
<button id="id_949">949</button>
<button id="id_950">950</button>
<button id="id_951">951</button>
<button id="id_952">952</button>
<button id="id_953">953</button>
<button id="id_954">954</button>
<button id="id_955">955</button>
<button id="id_956">956</button>
<button id="id_957">957</button>
<button id="id_958">958</button>
<button id="id_959">959</button>
<button id="id_960">960</button>
<button id="id_961">961</button>
<button id="id_962">962</button>
<button id="id_963">963</button>
<button id="id_964">964</button>
<button id="id_965">965</button>
<button id="id_966">966</button>
<button id="id_967">967</button>
<button id="id_968">968</button>
<button id="id_969">969</button>
<button id="id_970">970</button>
<button id="id_971">971</button>
<button id="id_972">972</button>
<button id="id_973">973</button>
<button id="id_974">974</button>
<button id="id_975">975</button>
<button id="id_976">976</button>
<button id="id_977">977</button>
<button id="id_978">978</button>
<button id="id_979">979</button>
<button id="id_980">980</button>
<button id="id_981">981</button>
<button id="id_982">982</button>
<button id="id_983">983</button>
<button id="id_984">984</button>
<button id="id_985">985</button>
<button id="id_986">986</button>
<button id="id_987">987</button>
<button id="id_988">988</button>
<button id="id_989">989</button>
<button id="id_990">990</button>
<button id="id_991">991</button>
<button id="id_992">992</button>
<button id="id_993">993</button>
<button id="id_994">994</button>
<button id="id_995">995</button>
<button id="id_996">996</button>
<button id="id_997">997</button>
<button id="id_998">998</button>
<button id="id_999">999</button>
<button id="id_1000">1000</button>   
        
        </body>


    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
